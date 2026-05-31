import type { SearchResult, YearMatch, Person, HistoricalEvent } from '@/lib/types';
import { people, events, regions } from '@/data/mockData';

/**
 * Search across all entities: people, events, regions, years.
 * Supports Chinese names, English names, aliases, tags, and year numbers.
 * Only returns published data for public-facing search.
 */
export function search(query: string): SearchResult {
  const q = query.trim();
  if (!q) {
    return { people: [], events: [], regions: [], yearMatches: [] };
  }

  const results: SearchResult = {
    people: searchPeople(q),
    events: searchEvents(q),
    regions: searchRegions(q),
    yearMatches: searchYears(q),
  };

  return results;
}

function matchScore(text: string, query: string): number {
  const lower = text.toLowerCase();
  const q = query.toLowerCase();
  if (lower === q) return 100;
  if (lower.startsWith(q)) return 80;
  if (lower.includes(q)) return 40;
  return 0;
}

function searchPeople(q: string): Person[] {
  const publishedPeople = people.filter((p) => p.dataStatus === 'published');

  const results = publishedPeople
    .map((p) => {
      let score = 0;
      score += matchScore(p.name, q) * 3;
      score += matchScore(p.nameEn ?? '', q) * 3;
      for (const alt of p.alternativeNames) {
        score += matchScore(alt, q) * 2;
      }
      for (const tag of p.tags) {
        score += matchScore(tag, q);
      }
      score += matchScore(p.summary ?? '', q) * 0.5;
      score += matchScore(p.summaryEn ?? '', q) * 0.5;
      return { person: p, score };
    })
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.person);

  return results;
}

function searchEvents(q: string): HistoricalEvent[] {
  const publishedEvents = events.filter((e) => e.dataStatus === 'published');

  const results = publishedEvents
    .map((e) => {
      let score = 0;
      score += matchScore(e.title, q) * 3;
      score += matchScore(e.titleEn ?? '', q) * 3;
      score += matchScore(e.summary ?? '', q) * 2;
      score += matchScore(e.summaryEn ?? '', q) * 2;
      for (const tag of e.tags) {
        score += matchScore(tag, q);
      }
      if (e.placeName) {
        score += matchScore(e.placeName, q);
        score += matchScore(e.placeNameEn ?? '', q);
      }
      return { event: e, score };
    })
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.event);

  return results;
}

function searchRegions(q: string) {
  return regions
    .map((r) => {
      let score = 0;
      score += matchScore(r.name, q) * 3;
      score += matchScore(r.nameEn ?? '', q) * 3;
      if (r.description) {
        score += matchScore(r.description, q);
        score += matchScore(r.descriptionEn ?? '', q);
      }
      return { region: r, score };
    })
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.region);
}

function searchYears(q: string): YearMatch[] {
  const publishedEvents = events.filter((e) => e.dataStatus === 'published');

  // Try to parse as a year number
  const yearNum = parseInt(q, 10);
  if (isNaN(yearNum)) return [];

  const range = 20; // Look at ±20 years
  const inRange = publishedEvents.filter((e) => {
    const eventStart = e.startYear ?? 0;
    const eventEnd = e.endYear ?? eventStart;
    return (
      Math.abs(eventStart - yearNum) <= range ||
      Math.abs(eventEnd - yearNum) <= range ||
      (eventStart <= yearNum && eventEnd >= yearNum)
    );
  });

  if (inRange.length === 0) {
    // Only show if the year exists in our data range
    const allYears = publishedEvents.map((e) => e.startYear ?? 0);
    const minYear = Math.min(...allYears);
    const maxYear = Math.max(...allYears);
    if (yearNum < minYear || yearNum > maxYear) return [];
  }

  return [
    {
      year: yearNum,
      nearEvents: inRange,
      label: `${yearNum}年前后的事件`,
    },
  ];
}
