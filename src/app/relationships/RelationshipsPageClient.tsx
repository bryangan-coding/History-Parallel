'use client';

import { useState, useMemo, useCallback, useRef, useEffect } from 'react';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, personSummary, regionName } from '@/lib/types';
import type { Person, Region } from '@/lib/types';
import type { Relationship } from '@/data/relationships';

// Region-to-color mapping (grouped by continent)
const REGION_COLORS: Record<string, string> = {
  // Asia — warm tones
  asia: '#b91c1c',
  china: '#b91c1c',
  'song-dynasty': '#b91c1c',
  'tang-dynasty': '#b91c1c',
  'ming-dynasty': '#b91c1c',
  india: '#d97706',
  japan: '#0891b2',
  'middle-east': '#b45309',
  seljuk: '#b45309',
  'mongol-empire': '#dc2626',
  // Europe — cool tones
  europe: '#1d4ed8',
  england: '#2563eb',
  byzantine: '#7c3aed',
  'renaissance-europe': '#4f46e5',
  'roman-empire': '#4338ca',
  // Africa
  africa: '#059669',
  // Americas
  americas: '#0d9488',
};

const RELATIONSHIP_TYPES = [
  { value: 'mentor-student', label: '师徒', labelEn: 'Mentor-Student', color: '#059669', icon: '📚' },
  { value: 'contemporary', label: '同时代', labelEn: 'Contemporary', color: '#6366f1', icon: '🌍' },
  { value: 'influenced-by', label: '影响', labelEn: 'Influenced By', color: '#d97706', icon: '💡' },
  { value: 'rival', label: '对手', labelEn: 'Rival', color: '#dc2626', icon: '⚔️' },
  { value: 'family', label: '亲属', labelEn: 'Family', color: '#ec4899', icon: '👨‍👩‍👦' },
] as const;

const ERAS = [
  { value: 'bce', label: '公元前', labelEn: 'BCE', min: -Infinity, max: 0 },
  { value: '1-10c', label: '1-10世纪', labelEn: '1st-10th C', min: 1, max: 1000 },
  { value: '11-15c', label: '11-15世纪', labelEn: '11th-15th C', min: 1001, max: 1500 },
  { value: '15c-plus', label: '15世纪后', labelEn: '15th C+', min: 1500, max: Infinity },
] as const;

function getRegionColor(regionId?: string): string {
  if (!regionId) return '#78716c';
  return REGION_COLORS[regionId] || '#78716c';
}

// Force-directed layout with improved spacing to reduce overlap
function runForceLayout(
  nodes: Array<{ id: string; x: number; y: number; vx: number; vy: number }>,
  edges: Array<{ source: string; target: string }>,
  width: number,
  height: number
) {
  const nodeCount = nodes.length;
  // Stronger repulsion for dense graphs
  const repulsionStrength = nodeCount > 30 ? 6000 : 3000;
  const attractionStrength = 0.005;
  const damping = 0.8;
  const iterations = 150;
  // Minimum distance between any two node centers (prevent label overlap)
  const minNodeDist = 70;

  // Build adjacency map for faster edge lookups
  const adjMap = new Map<string, Set<string>>();
  for (const edge of edges) {
    if (!adjMap.has(edge.source)) adjMap.set(edge.source, new Set());
    if (!adjMap.has(edge.target)) adjMap.set(edge.target, new Set());
    adjMap.get(edge.source)!.add(edge.target);
    adjMap.get(edge.target)!.add(edge.source);
  }

  for (let iter = 0; iter < iterations; iter++) {
    // Cooling factor: gradually reduce movement for stability
    const cooling = 1 - iter / iterations;

    // Repulsion between all pairs
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
        // Stronger short-range repulsion to prevent overlap
        const force = repulsionStrength / (dist * dist);
        const fx = (dx / dist) * force * cooling;
        const fy = (dy / dist) * force * cooling;
        nodes[i].vx += fx;
        nodes[i].vy += fy;
        nodes[j].vx -= fx;
        nodes[j].vy -= fy;
      }
    }

    // Attraction along edges
    for (const edge of edges) {
      const source = nodes.find((n) => n.id === edge.source);
      const target = nodes.find((n) => n.id === edge.target);
      if (!source || !target) continue;
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      // Ideal edge length based on graph density
      const idealLen = Math.min(200, Math.max(100, Math.min(width, height) / Math.sqrt(nodeCount) * 1.5));
      const displacement = dist - idealLen;
      const force = displacement * attractionStrength;
      const fx = (dx / Math.max(dist, 1)) * force * cooling;
      const fy = (dy / Math.max(dist, 1)) * force * cooling;
      source.vx += fx;
      source.vy += fy;
      target.vx -= fx;
      target.vy -= fy;
    }

    // Center gravity (weaker for large graphs to allow spread)
    const cx = width / 2;
    const cy = height / 2;
    const gravityStrength = 0.0005;
    for (const node of nodes) {
      node.vx += (cx - node.x) * gravityStrength;
      node.vy += (cy - node.y) * gravityStrength;
    }

    // Apply velocities with damping and speed limit
    const maxSpeed = 10;
    for (const node of nodes) {
      node.vx *= damping;
      node.vy *= damping;
      // Clamp velocity
      const speed = Math.sqrt(node.vx * node.vx + node.vy * node.vy);
      if (speed > maxSpeed) {
        node.vx = (node.vx / speed) * maxSpeed;
        node.vy = (node.vy / speed) * maxSpeed;
      }
      node.x += node.vx;
      node.y += node.vy;
      // Keep within bounds with padding
      const padding = 60;
      node.x = Math.max(padding, Math.min(width - padding, node.x));
      node.y = Math.max(padding, Math.min(height - padding, node.y));
    }
  }

  // Post-processing: resolve remaining overlaps
  for (let pass = 0; pass < 3; pass++) {
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < minNodeDist && dist > 0) {
          const overlap = (minNodeDist - dist) / 2;
          const nx = dx / dist;
          const ny = dy / dist;
          nodes[i].x += nx * overlap;
          nodes[i].y += ny * overlap;
          nodes[j].x -= nx * overlap;
          nodes[j].y -= ny * overlap;
        }
      }
    }
  }

  return nodes;
}

interface RelationshipsPageClientProps {
  personMap: Map<string, Person>;
  regionMap: Map<string, Region>;
  relationships: Relationship[];
}

type ViewMode = 'cards' | 'graph';

export default function RelationshipsPageClient({
  personMap,
  regionMap,
  relationships: allRelationships,
}: RelationshipsPageClientProps) {
  const { locale } = useLocale();
  const svgRef = useRef<SVGSVGElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  // View mode: default to 'cards' for better readability
  const [viewMode, setViewMode] = useState<ViewMode>('cards');

  // Card view state
  const [expandedType, setExpandedType] = useState<string | null>(null);
  const [selectedPerson, setSelectedPerson] = useState<Person | null>(null);

  // Graph view state
  const [selectedTypes, setSelectedTypes] = useState<Set<string>>(
    new Set(RELATIONSHIP_TYPES.map((rt) => rt.value))
  );
  const [selectedRegion, setSelectedRegion] = useState<string>('all');
  const [selectedEra, setSelectedEra] = useState<string>('all');
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);
  const [graphLayout, setGraphLayout] = useState<{
    nodes: Array<{ id: string; x: number; y: number; vx: number; vy: number }>;
    edges: Relationship[];
  }>({ nodes: [], edges: [] });

  // --- Group relationships by type for card view ---
  // Only include relationships where both people exist in the database
  const validRelationships = useMemo(() => {
    return allRelationships.filter(
      (rel) => personMap.has(rel.personId1) && personMap.has(rel.personId2)
    );
  }, [allRelationships, personMap]);

  const relationshipsByType = useMemo(() => {
    const grouped = new Map<string, Relationship[]>();
    validRelationships.forEach((rel) => {
      const list = grouped.get(rel.type) || [];
      list.push(rel);
      grouped.set(rel.type, list);
    });
    return grouped;
  }, [validRelationships]);

  // Get top relationships per type (show only first N by default, expand to show all)
  const INITIAL_SHOW_COUNT = 4;

  // Get unique regions for filter (graph view)
  const regionOptions = useMemo(() => {
    const regionSet = new Map<string, string>();
    personMap.forEach((person) => {
      if (person.regionId) {
        const region = regionMap.get(person.regionId);
        if (region) {
          const topId = region.parentRegionId || region.id;
          regionSet.set(topId, regionName(region, locale));
        }
      }
    });
    return Array.from(regionSet.entries()).map(([id, name]) => ({ id, name }));
  }, [personMap, regionMap, locale]);

  // --- Graph view logic ---
  const filteredRelationships = useMemo(() => {
    return allRelationships.filter((rel) => {
      if (!selectedTypes.has(rel.type)) return false;

      // Both people must exist in personMap (DB may be missing some)
      const p1 = personMap.get(rel.personId1);
      const p2 = personMap.get(rel.personId2);
      if (!p1 || !p2) return false;

      if (selectedRegion !== 'all') {
        const p1TopRegion = p1.regionId
          ? regionMap.get(p1.regionId)?.parentRegionId || p1.regionId
          : null;
        const p2TopRegion = p2.regionId
          ? regionMap.get(p2.regionId)?.parentRegionId || p2.regionId
          : null;
        if (p1TopRegion !== selectedRegion && p2TopRegion !== selectedRegion) return false;
      }

      if (selectedEra !== 'all') {
        const era = ERAS.find((e) => e.value === selectedEra);
        if (era) {
          const year1 = p1.birthYear ?? p1.deathYear ?? 0;
          const year2 = p2.birthYear ?? p2.deathYear ?? 0;
          const inEra1 = year1 >= era.min && year1 <= era.max;
          const inEra2 = year2 >= era.min && year2 <= era.max;
          if (!inEra1 && !inEra2) return false;
        }
      }

      return true;
    });
  }, [selectedTypes, selectedRegion, selectedEra, personMap, regionMap, allRelationships]);

  const hoveredConnections = useMemo(() => {
    if (!hoveredNode) return new Set<string>();
    const connected = new Set<string>([hoveredNode]);
    filteredRelationships.forEach((rel) => {
      if (rel.personId1 === hoveredNode) connected.add(rel.personId2);
      if (rel.personId2 === hoveredNode) connected.add(rel.personId1);
    });
    return connected;
  }, [hoveredNode, filteredRelationships]);

  const updateLayout = useCallback(() => {
    if (!containerRef.current) return;
    const width = containerRef.current.clientWidth;
    // Taller canvas to give nodes more breathing room
    const height = Math.max(700, Math.min(900, filteredRelationships.length * 8));

    const nodeIds = new Set<string>();
    filteredRelationships.forEach((rel) => {
      nodeIds.add(rel.personId1);
      nodeIds.add(rel.personId2);
    });

    const circleR = 200;
    const angleStep = (2 * Math.PI) / Math.max(nodeIds.size, 1);
    let idx = 0;

    const nodes = Array.from(nodeIds).map((id) => {
      const angle = idx * angleStep;
      idx++;
      return {
        id,
        x: width / 2 + circleR * Math.cos(angle) + (Math.random() - 0.5) * 50,
        y: height / 2 + circleR * Math.sin(angle) + (Math.random() - 0.5) * 50,
        vx: 0,
        vy: 0,
      };
    });

    const edges = filteredRelationships.map((rel) => ({
      source: rel.personId1,
      target: rel.personId2,
    }));

    const laidOut = runForceLayout(nodes, edges, width, height);
    setGraphLayout({ nodes: laidOut, edges: filteredRelationships });
  }, [filteredRelationships]);

  useEffect(() => {
    if (viewMode === 'graph') {
      updateLayout();
    }
  }, [viewMode, updateLayout]);

  useEffect(() => {
    const handleResize = () => {
      if (viewMode === 'graph') updateLayout();
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [viewMode, updateLayout]);

  const toggleType = (type: string) => {
    setSelectedTypes((prev) => {
      const next = new Set(prev);
      if (next.has(type)) next.delete(type);
      else next.add(type);
      return next;
    });
  };

  const handlePersonClick = (id: string) => {
    const person = personMap.get(id);
    if (person) setSelectedPerson(selectedPerson?.id === id ? null : person);
  };

  const svgHeight = Math.max(700, Math.min(900, filteredRelationships.length * 8));
  const isGraphRendering = graphLayout.nodes.length === 0;

  // Get person's relationships for detail panel
  const personRelationships = useMemo(() => {
    if (!selectedPerson) return [];
    return validRelationships.filter(
      (r) => r.personId1 === selectedPerson.id || r.personId2 === selectedPerson.id
    );
  }, [selectedPerson, validRelationships]);

  return (
    <div>
      {/* Header */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-stone-900">
          {locale === 'en' ? 'Person Relationships' : '人物关系图'}
        </h1>
        <p className="mt-1 text-sm text-stone-500">
          {locale === 'en'
            ? 'Explore connections between historical figures across civilizations'
            : '探索跨越文明的历史人物关系网络'}
        </p>
      </div>

      {/* View mode toggle */}
      <div className="flex items-center gap-2 mb-6">
        <span className="text-xs font-semibold text-stone-500 uppercase tracking-wide mr-2">
          {locale === 'en' ? 'View' : '视图'}
        </span>
        <div className="flex bg-stone-100 rounded-lg p-0.5">
          <button
            onClick={() => setViewMode('cards')}
            className={`px-4 py-1.5 text-sm rounded-md transition-colors ${
              viewMode === 'cards'
                ? 'bg-white text-stone-900 shadow-sm font-medium'
                : 'text-stone-500 hover:text-stone-700'
            }`}
          >
            {locale === 'en' ? 'By Category' : '分类浏览'}
          </button>
          <button
            onClick={() => setViewMode('graph')}
            className={`px-4 py-1.5 text-sm rounded-md transition-colors ${
              viewMode === 'graph'
                ? 'bg-white text-stone-900 shadow-sm font-medium'
                : 'text-stone-500 hover:text-stone-700'
            }`}
          >
            {locale === 'en' ? 'Relation Graph' : '关系图谱'}
          </button>
        </div>
        <span className="text-xs text-stone-400 ml-auto">
          {locale === 'en'
            ? `${validRelationships.length} relationships · ${personMap.size} people`
            : `${validRelationships.length} 条关系 · ${personMap.size} 位人物`}
        </span>
      </div>

      {/* ==================== CARD VIEW ==================== */}
      {viewMode === 'cards' && (
        <div className="space-y-6">
          {RELATIONSHIP_TYPES.map((rt) => {
            const rels = relationshipsByType.get(rt.value) || [];
            const isExpanded = expandedType === rt.value;
            const displayRels = isExpanded ? rels : rels.slice(0, INITIAL_SHOW_COUNT);
            const hasMore = rels.length > INITIAL_SHOW_COUNT;

            return (
              <div
                key={rt.value}
                className="border border-stone-200 rounded-xl bg-white overflow-hidden"
              >
                {/* Type header */}
                <div
                  className="flex items-center gap-3 px-5 py-4 border-b border-stone-100"
                  style={{ borderLeftColor: rt.color, borderLeftWidth: 3, borderLeftStyle: 'solid' }}
                >
                  <span className="text-lg">{rt.icon}</span>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-stone-800">
                      {locale === 'en' ? rt.labelEn : rt.label}
                    </h3>
                    <p className="text-xs text-stone-400 mt-0.5">
                      {locale === 'en'
                        ? `${rels.length} connection${rels.length > 1 ? 's' : ''}`
                        : `${rels.length} 组关系`}
                    </p>
                  </div>
                </div>

                {/* Relationship list */}
                <div className="divide-y divide-stone-50">
                  {displayRels.map((rel) => {
                    const p1 = personMap.get(rel.personId1);
                    const p2 = personMap.get(rel.personId2);
                    if (!p1 || !p2) return null;

                    const description = locale === 'en' ? rel.descriptionEn : rel.description;

                    // For influenced-by, the display order should be: influencer → influenced
                    // personId2 is the influencer, personId1 is the influenced
                    const isInfluencedBy = rel.type === 'influenced-by';
                    const displayP1 = isInfluencedBy ? p2 : p1;
                    const displayP2 = isInfluencedBy ? p1 : p2;
                    const displayId1 = isInfluencedBy ? rel.personId2 : rel.personId1;
                    const displayId2 = isInfluencedBy ? rel.personId1 : rel.personId2;

                    return (
                      <div key={rel.id} className="px-5 py-3 hover:bg-stone-50 transition-colors">
                        <div className="flex items-center gap-3 mb-1">
                          {/* Person 1 (source of relationship) */}
                          <button
                            onClick={() => handlePersonClick(displayId1)}
                            className="flex items-center gap-2 group"
                          >
                            <span
                              className="inline-block w-2.5 h-2.5 rounded-full shrink-0"
                              style={{ backgroundColor: getRegionColor(displayP1.regionId) }}
                            />
                            <span className="text-sm font-medium text-stone-800 group-hover:text-stone-600 transition-colors">
                              {personName(displayP1, locale)}
                            </span>
                            {(displayP1.birthYear || displayP1.deathYear) && (
                              <span className="text-xs text-stone-400">
                                {displayP1.birthYear}{displayP1.deathYear ? `-${displayP1.deathYear}` : ''}
                              </span>
                            )}
                            {displayP1.regionId && (
                              <span className="text-xs text-stone-400">
                                {regionName(regionMap.get(displayP1.regionId)!, locale)}
                              </span>
                            )}
                          </button>

                          {/* Connector with direction */}
                          <span className="flex items-center gap-1 shrink-0">
                            {rt.value !== 'contemporary' && rt.value !== 'rival' && (
                              <svg width="10" height="10" viewBox="0 0 10 10" className="shrink-0">
                                <polygon points="0,2 8,5 0,8" fill={rt.color} opacity={0.6} />
                              </svg>
                            )}
                            <span className="text-xs px-2 py-0.5 rounded-full font-medium"
                              style={{
                                backgroundColor: rt.color + '18',
                                color: rt.color,
                                fontSize: 10,
                              }}
                            >
                              {locale === 'en' ? rt.labelEn : rt.label}
                            </span>
                          </span>

                          {/* Person 2 (target of relationship) */}
                          <button
                            onClick={() => handlePersonClick(displayId2)}
                            className="flex items-center gap-2 group"
                          >
                            <span
                              className="inline-block w-2.5 h-2.5 rounded-full shrink-0"
                              style={{ backgroundColor: getRegionColor(displayP2.regionId) }}
                            />
                            <span className="text-sm font-medium text-stone-800 group-hover:text-stone-600 transition-colors">
                              {personName(displayP2, locale)}
                            </span>
                            {(displayP2.birthYear || displayP2.deathYear) && (
                              <span className="text-xs text-stone-400">
                                {displayP2.birthYear}{displayP2.deathYear ? `-${displayP2.deathYear}` : ''}
                              </span>
                            )}
                            {displayP2.regionId && (
                              <span className="text-xs text-stone-400">
                                {regionName(regionMap.get(displayP2.regionId)!, locale)}
                              </span>
                            )}
                          </button>
                        </div>

                        {/* Description */}
                        {description && (
                          <p className="text-xs text-stone-500 leading-relaxed ml-0 pl-0">
                            {description}
                          </p>
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Show more / less */}
                {hasMore && (
                  <button
                    onClick={() =>
                      setExpandedType(isExpanded ? null : rt.value)
                    }
                    className="w-full px-5 py-2.5 text-xs text-stone-500 hover:text-stone-700 hover:bg-stone-50 transition-colors text-center"
                  >
                    {isExpanded
                      ? locale === 'en'
                        ? 'Show less'
                        : '收起'
                      : locale === 'en'
                        ? `Show all ${rels.length} connections`
                        : `查看全部 ${rels.length} 组关系`}
                  </button>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* ==================== GRAPH VIEW ==================== */}
      {viewMode === 'graph' && (
        <div className="flex flex-col lg:flex-row gap-6">
          {/* Sidebar */}
          <div className="lg:w-64 shrink-0 space-y-5">
            {/* Relationship type filter */}
            <div>
              <h3 className="text-xs font-semibold text-stone-500 uppercase tracking-wide mb-2">
                {locale === 'en' ? 'Relationship Type' : '关系类型'}
              </h3>
              <div className="space-y-1">
                {RELATIONSHIP_TYPES.map((rt) => (
                  <label
                    key={rt.value}
                    className="flex items-center gap-2 text-sm text-stone-600 cursor-pointer hover:text-stone-800"
                  >
                    <input
                      type="checkbox"
                      checked={selectedTypes.has(rt.value)}
                      onChange={() => toggleType(rt.value)}
                      className="rounded border-stone-300 text-stone-600 focus:ring-stone-500"
                    />
                    {locale === 'en' ? rt.labelEn : rt.label}
                  </label>
                ))}
              </div>
            </div>

            {/* Region filter */}
            <div>
              <h3 className="text-xs font-semibold text-stone-500 uppercase tracking-wide mb-2">
                {locale === 'en' ? 'Region' : '地区'}
              </h3>
              <select
                value={selectedRegion}
                onChange={(e) => setSelectedRegion(e.target.value)}
                className="w-full text-sm border border-stone-200 rounded-lg px-3 py-2 bg-white text-stone-700 focus:outline-none focus:border-stone-400"
              >
                <option value="all">{locale === 'en' ? 'All Regions' : '全部地区'}</option>
                {regionOptions.map((r) => (
                  <option key={r.id} value={r.id}>
                    {r.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Era filter */}
            <div>
              <h3 className="text-xs font-semibold text-stone-500 uppercase tracking-wide mb-2">
                {locale === 'en' ? 'Era' : '时代'}
              </h3>
              <select
                value={selectedEra}
                onChange={(e) => setSelectedEra(e.target.value)}
                className="w-full text-sm border border-stone-200 rounded-lg px-3 py-2 bg-white text-stone-700 focus:outline-none focus:border-stone-400"
              >
                <option value="all">{locale === 'en' ? 'All Eras' : '全部时代'}</option>
                {ERAS.map((e) => (
                  <option key={e.value} value={e.value}>
                    {locale === 'en' ? e.labelEn : e.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Graph */}
          <div className="flex-1 min-w-0">
            <div
              ref={containerRef}
              className="relative border border-stone-200 rounded-xl bg-white overflow-hidden"
            >
              {isGraphRendering ? (
                <div className="flex items-center justify-center" style={{ height: svgHeight }}>
                  <div className="animate-spin w-8 h-8 border-2 border-stone-300 border-t-stone-600 rounded-full" />
                </div>
              ) : (
                <svg
                  ref={svgRef}
                  width="100%"
                  height={svgHeight}
                  viewBox={`0 0 ${containerRef.current?.clientWidth || 800} ${svgHeight}`}
                  className="w-full"
                >
                  {/* Edges */}
                  {graphLayout.edges.map((rel) => {
                    const sourceNode = graphLayout.nodes.find((n) => n.id === rel.personId1);
                    const targetNode = graphLayout.nodes.find((n) => n.id === rel.personId2);
                    if (!sourceNode || !targetNode) return null;

                    const isHighlighted =
                      !hoveredNode ||
                      hoveredConnections.has(rel.personId1) ||
                      hoveredConnections.has(rel.personId2);
                    const opacity = isHighlighted ? 0.7 : 0.1;

                    const typeColors: Record<string, string> = {
                      'mentor-student': '#059669',
                      contemporary: '#6366f1',
                      'influenced-by': '#d97706',
                      rival: '#dc2626',
                      family: '#ec4899',
                    };
                    const strokeColor = typeColors[rel.type] || '#94a3b8';

                    // Determine directionality
                    // mentor-student: personId1 (teacher) → personId2 (student)
                    // influenced-by: personId2 (influencer) → personId1 (influenced)
                    // family: personId1 → personId2
                    // contemporary, rival: no arrow (undirected)
                    const hasArrow = rel.type !== 'contemporary' && rel.type !== 'rival';
                    let arrowFrom = sourceNode;
                    let arrowTo = targetNode;
                    if (rel.type === 'influenced-by') {
                      // Arrow points from influencer (personId2) to influenced (personId1)
                      arrowFrom = targetNode;
                      arrowTo = sourceNode;
                    }

                    // Calculate line with node radius offset
                    const nodeRadius = 22;
                    const dx = arrowTo.x - arrowFrom.x;
                    const dy = arrowTo.y - arrowFrom.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 1) return null;
                    const nx = dx / dist;
                    const ny = dy / dist;

                    const x1 = arrowFrom.x + nx * nodeRadius;
                    const y1 = arrowFrom.y + ny * nodeRadius;
                    const x2 = arrowTo.x - nx * nodeRadius;
                    const y2 = arrowTo.y - ny * nodeRadius;

                    // Arrowhead
                    const arrowSize = 8;
                    const arrowAngle = Math.PI / 6; // 30 degrees
                    const arrowBaseX = x2 - nx * arrowSize;
                    const arrowBaseY = y2 - ny * arrowSize;
                    const ax1 = x2 - nx * arrowSize * Math.cos(arrowAngle) + ny * arrowSize * Math.sin(arrowAngle);
                    const ay1 = y2 - ny * arrowSize * Math.cos(arrowAngle) - nx * arrowSize * Math.sin(arrowAngle);
                    const ax2 = x2 - nx * arrowSize * Math.cos(arrowAngle) - ny * arrowSize * Math.sin(arrowAngle);
                    const ay2 = y2 - ny * arrowSize * Math.cos(arrowAngle) + nx * arrowSize * Math.sin(arrowAngle);

                    const isDashed = rel.type === 'contemporary';

                    return (
                      <g key={rel.id}>
                        {/* Edge line */}
                        <line
                          x1={x1}
                          y1={y1}
                          x2={hasArrow ? arrowBaseX : x2}
                          y2={hasArrow ? arrowBaseY : y2}
                          stroke={strokeColor}
                          strokeWidth={1.5}
                          opacity={opacity}
                          strokeDasharray={isDashed ? '4,4' : undefined}
                        />
                        {/* Arrowhead */}
                        {hasArrow && (
                          <polygon
                            points={`${x2},${y2} ${ax1},${ay1} ${ax2},${ay2}`}
                            fill={strokeColor}
                            opacity={opacity}
                          />
                        )}
                        {/* Edge label */}
                        {isHighlighted && (
                          <text
                            x={(sourceNode.x + targetNode.x) / 2}
                            y={(sourceNode.y + targetNode.y) / 2 - 8}
                            textAnchor="middle"
                            className="pointer-events-none select-none"
                            style={{ fontSize: 10, fill: strokeColor, fontWeight: 500 }}
                          >
                            {RELATIONSHIP_TYPES.find((rt) => rt.value === rel.type)
                              ?.label || rel.type}
                          </text>
                        )}
                      </g>
                    );
                  })}

                  {/* Nodes */}
                  {graphLayout.nodes.map((node) => {
                    const person = personMap.get(node.id);
                    if (!person) return null;

                    const isHighlighted =
                      !hoveredNode || hoveredConnections.has(node.id);
                    const opacity = isHighlighted ? 1 : 0.2;
                    const color = getRegionColor(person.regionId);
                    const isSelected = selectedPerson?.id === node.id;
                    const radius = isSelected ? 28 : 22;

                    return (
                      <g
                        key={node.id}
                        onClick={() => handlePersonClick(node.id)}
                        onMouseEnter={() => setHoveredNode(node.id)}
                        onMouseLeave={() => setHoveredNode(null)}
                        className="cursor-pointer"
                        opacity={opacity}
                        style={{ transition: 'opacity 0.2s' }}
                      >
                        <circle
                          cx={node.x}
                          cy={node.y}
                          r={radius}
                          fill={color}
                          stroke={isSelected ? '#292524' : '#fff'}
                          strokeWidth={isSelected ? 3 : 2}
                        />
                        <text
                          x={node.x}
                          y={node.y + 4}
                          textAnchor="middle"
                          className="pointer-events-none select-none"
                          style={{ fontSize: 10, fontWeight: 500, fill: '#fff' }}
                        >
                          {personName(person, locale).length > 4
                            ? personName(person, locale).slice(0, 4) + '..'
                            : personName(person, locale)}
                        </text>
                        <text
                          x={node.x}
                          y={node.y + radius + 14}
                          textAnchor="middle"
                          className="pointer-events-none select-none"
                          style={{ fontSize: 11, fill: '#44403c' }}
                        >
                          {personName(person, locale)}
                        </text>
                      </g>
                    );
                  })}
                </svg>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Person detail panel (shared between views) */}
      {selectedPerson && (
        <div className="mt-6 p-6 border border-stone-200 rounded-xl bg-white">
          <div className="flex items-start justify-between">
            <div>
              <h3 className="text-lg font-semibold text-stone-900">
                {personName(selectedPerson, locale)}
              </h3>
              {selectedPerson.regionId && (
                <span className="inline-block mt-1 text-xs px-2 py-0.5 rounded border border-stone-200 bg-stone-50 text-stone-500">
                  {regionName(
                    regionMap.get(selectedPerson.regionId)!,
                    locale
                  )}
                </span>
              )}
            </div>
            <button
              onClick={() => setSelectedPerson(null)}
              className="text-stone-400 hover:text-stone-600 text-sm"
            >
              {locale === 'en' ? 'Close' : '关闭'}
            </button>
          </div>
          <p className="mt-2 text-sm text-stone-600">
            {selectedPerson.birthYear && selectedPerson.deathYear
              ? `${locale === 'en' ? 'Lived' : '生卒年'}：${selectedPerson.birthYear} - ${selectedPerson.deathYear}`
              : ''}
          </p>
          <p className="mt-3 text-sm text-stone-600 leading-relaxed">
            {personSummary(selectedPerson, locale)}
          </p>
          {/* Related connections */}
          <div className="mt-4">
            <h4 className="text-xs font-semibold text-stone-500 uppercase tracking-wide mb-2">
              {locale === 'en' ? 'Connections' : '关联人物'}
            </h4>
            <div className="flex flex-wrap gap-2">
              {personRelationships.map((rel) => {
                const otherId =
                  rel.personId1 === selectedPerson.id ? rel.personId2 : rel.personId1;
                const other = personMap.get(otherId);
                const typeLabel =
                  RELATIONSHIP_TYPES.find((rt) => rt.value === rel.type)?.label ||
                  rel.type;
                if (!other) return null;
                return (
                  <button
                    key={rel.id}
                    onClick={() => handlePersonClick(otherId)}
                    className="text-xs px-2 py-1 rounded border border-stone-200 bg-stone-50 hover:bg-stone-100 text-stone-600 transition-colors"
                  >
                    {typeLabel}: {personName(other, locale)}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
