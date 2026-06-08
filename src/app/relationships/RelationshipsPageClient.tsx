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
  { value: 'mentor-student', label: '师徒', labelEn: 'Mentor-Student' },
  { value: 'contemporary', label: '同时代', labelEn: 'Contemporary' },
  { value: 'influenced-by', label: '影响', labelEn: 'Influenced By' },
  { value: 'rival', label: '对手', labelEn: 'Rival' },
  { value: 'family', label: '亲属', labelEn: 'Family' },
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

// Force-directed layout
function runForceLayout(
  nodes: Array<{ id: string; x: number; y: number; vx: number; vy: number }>,
  edges: Array<{ source: string; target: string }>,
  width: number,
  height: number
) {
  const repulsionStrength = 3000;
  const attractionStrength = 0.01;
  const damping = 0.85;
  const iterations = 100;

  for (let iter = 0; iter < iterations; iter++) {
    // Repulsion between all pairs
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
        const force = repulsionStrength / (dist * dist);
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;
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
      const force = dist * attractionStrength;
      const fx = (dx / Math.max(dist, 1)) * force;
      const fy = (dy / Math.max(dist, 1)) * force;
      source.vx += fx;
      source.vy += fy;
      target.vx -= fx;
      target.vy -= fy;
    }

    // Center gravity
    const cx = width / 2;
    const cy = height / 2;
    for (const node of nodes) {
      node.vx += (cx - node.x) * 0.001;
      node.vy += (cy - node.y) * 0.001;
    }

    // Apply velocities with damping
    for (const node of nodes) {
      node.vx *= damping;
      node.vy *= damping;
      node.x += node.vx;
      node.y += node.vy;
      // Keep within bounds
      node.x = Math.max(40, Math.min(width - 40, node.x));
      node.y = Math.max(40, Math.min(height - 40, node.y));
    }
  }

  return nodes;
}

interface RelationshipsPageClientProps {
  personMap: Map<string, Person>;
  regionMap: Map<string, Region>;
  relationships: Relationship[];
}

export default function RelationshipsPageClient({
  personMap,
  regionMap,
  relationships: allRelationships,
}: RelationshipsPageClientProps) {
  const { locale, t } = useLocale();
  const svgRef = useRef<SVGSVGElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const [selectedTypes, setSelectedTypes] = useState<Set<string>>(
    new Set(RELATIONSHIP_TYPES.map((rt) => rt.value))
  );
  const [selectedRegion, setSelectedRegion] = useState<string>('all');
  const [selectedEra, setSelectedEra] = useState<string>('all');
  const [selectedPerson, setSelectedPerson] = useState<Person | null>(null);
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);
  const [layout, setLayout] = useState<{
    nodes: Array<{ id: string; x: number; y: number; vx: number; vy: number }>;
    edges: Relationship[];
  }>({ nodes: [], edges: [] });

  // Get unique regions for filter
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

  // Filter relationships
  const filteredRelationships = useMemo(() => {
    return allRelationships.filter((rel) => {
      if (!selectedTypes.has(rel.type)) return false;

      if (selectedRegion !== 'all') {
        const p1 = personMap.get(rel.personId1);
        const p2 = personMap.get(rel.personId2);
        const p1TopRegion = p1?.regionId
          ? regionMap.get(p1.regionId)?.parentRegionId || p1.regionId
          : null;
        const p2TopRegion = p2?.regionId
          ? regionMap.get(p2.regionId)?.parentRegionId || p2.regionId
          : null;
        if (p1TopRegion !== selectedRegion && p2TopRegion !== selectedRegion) return false;
      }

      if (selectedEra !== 'all') {
        const era = ERAS.find((e) => e.value === selectedEra);
        if (era) {
          const p1 = personMap.get(rel.personId1);
          const p2 = personMap.get(rel.personId2);
          const year1 = p1?.birthYear ?? p1?.deathYear ?? 0;
          const year2 = p2?.birthYear ?? p2?.deathYear ?? 0;
          const inEra1 = year1 >= era.min && year1 <= era.max;
          const inEra2 = year2 >= era.min && year2 <= era.max;
          if (!inEra1 && !inEra2) return false;
        }
      }

      return true;
    });
  }, [selectedTypes, selectedRegion, selectedEra, personMap, regionMap, allRelationships]);

  // Get connected node IDs for hover highlighting
  const hoveredConnections = useMemo(() => {
    if (!hoveredNode) return new Set<string>();
    const connected = new Set<string>([hoveredNode]);
    filteredRelationships.forEach((rel) => {
      if (rel.personId1 === hoveredNode) connected.add(rel.personId2);
      if (rel.personId2 === hoveredNode) connected.add(rel.personId1);
    });
    return connected;
  }, [hoveredNode, filteredRelationships]);

  // Update layout
  const updateLayout = useCallback(() => {
    if (!containerRef.current) return;
    const width = containerRef.current.clientWidth;
    const height = 600;

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
    setLayout({ nodes: laidOut, edges: filteredRelationships });
  }, [filteredRelationships]);

  useEffect(() => {
    updateLayout();
    const handleResize = () => updateLayout();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [updateLayout]);

  const toggleType = (type: string) => {
    setSelectedTypes((prev) => {
      const next = new Set(prev);
      if (next.has(type)) next.delete(type);
      else next.add(type);
      return next;
    });
  };

  const handleNodeClick = (id: string) => {
    const person = personMap.get(id);
    if (person) setSelectedPerson(selectedPerson?.id === id ? null : person);
  };

  const svgHeight = 600;
  const isRendering = layout.nodes.length === 0;

  return (
    <div>
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
            {isRendering ? (
              <div className="flex items-center justify-center h-[600px]">
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
                {layout.edges.map((rel) => {
                  const source = layout.nodes.find((n) => n.id === rel.personId1);
                  const target = layout.nodes.find((n) => n.id === rel.personId2);
                  if (!source || !target) return null;

                  const isHighlighted =
                    !hoveredNode ||
                    hoveredConnections.has(rel.personId1) ||
                    hoveredConnections.has(rel.personId2);
                  const opacity = isHighlighted ? 0.7 : 0.1;

                  // Relationship type color
                  const typeColors: Record<string, string> = {
                    'mentor-student': '#059669',
                    contemporary: '#6366f1',
                    'influenced-by': '#d97706',
                    rival: '#dc2626',
                    family: '#ec4899',
                  };

                  return (
                    <g key={rel.id}>
                      <line
                        x1={source.x}
                        y1={source.y}
                        x2={target.x}
                        y2={target.y}
                        stroke={typeColors[rel.type] || '#94a3b8'}
                        strokeWidth={1.5}
                        opacity={opacity}
                        strokeDasharray={rel.type === 'contemporary' ? '4,4' : undefined}
                      />
                      {/* Edge label */}
                      {isHighlighted && (
                        <text
                          x={(source.x + target.x) / 2}
                          y={(source.y + target.y) / 2 - 6}
                          textAnchor="middle"
                          className="text-[10px] fill-stone-500 pointer-events-none select-none"
                          style={{ fontSize: 10 }}
                        >
                          {RELATIONSHIP_TYPES.find((rt) => rt.value === rel.type)
                            ?.label || rel.type}
                        </text>
                      )}
                    </g>
                  );
                })}

                {/* Nodes */}
                {layout.nodes.map((node) => {
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
                      onClick={() => handleNodeClick(node.id)}
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
                      {/* Name label below node */}
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

      {/* Person detail panel */}
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
              {allRelationships.filter((r) => r.personId1 === selectedPerson.id || r.personId2 === selectedPerson.id).map((rel) => {
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
                    onClick={() => handleNodeClick(otherId)}
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
