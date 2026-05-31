/**
 * Wikidata response mapper.
 * Transforms raw SPARQL query results into our Person/Event types.
 */

import type { Person, HistoricalEvent, ExternalReference } from '../../src/lib/types';
import { normalizePersonName, normalizeEventTitle, normalizeTags } from '../../src/lib/normalization';
import { calculatePersonConfidenceScore, calculateEventConfidenceScore } from '../../src/lib/confidence';

interface WikidataBinding {
  type: string;
  value: string;
  'xml:lang'?: string;
}

type BindingMap = Record<string, WikidataBinding>;

/**
 * Map a Wikidata SPARQL result row to a Person entity.
 */
export function mapWikidataPerson(row: BindingMap): Person {
  const qid = getBindingValue(row, 'person');
  const name = getBindingValue(row, 'personLabel') ?? 'Unknown';
  const birthDate = getBindingValue(row, 'birthDate');
  const deathDate = getBindingValue(row, 'deathDate');
  const occupation = getBindingValue(row, 'occupationLabel');

  // Parse dates
  const birthYear = birthDate ? parseInt(birthDate.substring(0, 4), 10) : undefined;
  const deathYear = deathDate ? parseInt(deathDate.substring(0, 4), 10) : undefined;

  const externalRefs: ExternalReference[] = [];
  if (qid) {
    externalRefs.push({
      id: `ref-wd-${qid}`,
      sourceType: 'wikidata',
      externalId: qid,
      url: `https://www.wikidata.org/wiki/${qid}`,
      title: name,
      license: 'CC0',
      retrievedAt: new Date().toISOString(),
    });
  }

  const person: Person = {
    id: `wd-person-${qid ?? Date.now()}`,
    name: normalizePersonName(name),
    alternativeNames: [],
    birthYear,
    deathYear,
    occupations: occupation ? [occupation] : [],
    tags: [],
    sourceIds: [],
    dataStatus: 'imported',
    confidenceScore: 0.3,
    externalReferences: externalRefs,
  };

  // Calculate initial confidence score
  person.confidenceScore = calculatePersonConfidenceScore(person);

  return person;
}

/**
 * Map a Wikidata SPARQL result row to a HistoricalEvent entity.
 */
export function mapWikidataEvent(row: BindingMap): HistoricalEvent {
  const qid = getBindingValue(row, 'event');
  const title = getBindingValue(row, 'eventLabel') ?? 'Unknown Event';
  const pointInTime = getBindingValue(row, 'pointInTime');
  const place = getBindingValue(row, 'placeLabel');

  const startYear = pointInTime ? parseInt(pointInTime.substring(0, 4), 10) : undefined;

  const externalRefs: ExternalReference[] = [];
  if (qid) {
    externalRefs.push({
      id: `ref-wd-${qid}`,
      sourceType: 'wikidata',
      externalId: qid,
      url: `https://www.wikidata.org/wiki/${qid}`,
      title,
      license: 'CC0',
      retrievedAt: new Date().toISOString(),
    });
  }

  const event: HistoricalEvent = {
    id: `wd-event-${qid ?? Date.now()}`,
    title: normalizeEventTitle(title),
    startYear,
    datePrecision: startYear ? 'year' : 'unknown',
    isApproximate: false,
    placeName: place ?? undefined,
    personIds: [],
    tags: [],
    importance: 3,
    sourceIds: [],
    relatedEventIds: [],
    dataStatus: 'imported',
    confidenceScore: 0.3,
    externalReferences: externalRefs,
  };

  event.confidenceScore = calculateEventConfidenceScore(event);

  return event;
}

function getBindingValue(row: BindingMap, key: string): string | undefined {
  const binding = row[key];
  if (!binding) return undefined;
  // Prefer the full URL (entity ID) and extract the QID
  if (key === 'person' || key === 'event' || key === 'occupation') {
    const match = binding.value.match(/\/([QP]\d+)$/);
    if (match) return match[1];
  }
  return binding.value;
}
