import {
  calculateNameSimilarity,
  calculateEventTitleSimilarity,
  findPotentialDuplicatePersons,
  findPotentialDuplicateEvents,
} from '../dedupe';
import type { Person, HistoricalEvent } from '../types';

function makePerson(overrides: Partial<Person> = {}): Person {
  return {
    id: 'p-1',
    name: '苏轼',
    alternativeNames: ['苏东坡'],
    birthYear: 1037,
    deathYear: 1101,
    regionId: 'song-dynasty',
    occupations: ['文学家'],
    tags: [],
    sourceIds: [],
    dataStatus: 'published',
    confidenceScore: 0.9,
    externalReferences: [],
    ...overrides,
  };
}

function makeEvent(overrides: Partial<HistoricalEvent> = {}): HistoricalEvent {
  return {
    id: 'e-1',
    title: 'Test Event',
    startYear: 1070,
    endYear: 1085,
    datePrecision: 'range',
    isApproximate: false,
    regionId: 'test-region',
    placeName: 'Test Place',
    personIds: [],
    tags: ['war'],
    importance: 4,
    sourceIds: [],
    relatedEventIds: [],
    dataStatus: 'published',
    confidenceScore: 0.8,
    externalReferences: [],
    ...overrides,
  };
}

describe('calculateNameSimilarity', () => {
  test('identical names return 1', () => {
    expect(calculateNameSimilarity('苏轼', '苏轼')).toBe(1);
  });

  test('completely different names return low score', () => {
    const score = calculateNameSimilarity('苏轼', 'William');
    expect(score).toBeLessThan(0.3);
  });

  test('similar names return high score', () => {
    const score = calculateNameSimilarity('William the Conqueror', 'William I of England');
    expect(score).toBeGreaterThan(0.1);
  });

  test('empty strings return 0', () => {
    expect(calculateNameSimilarity('', 'Something')).toBe(0);
    expect(calculateNameSimilarity('Something', '')).toBe(0);
  });
});

describe('findPotentialDuplicatePersons', () => {
  test('same Wikidata QID is strongest signal', () => {
    const person = makePerson({ id: 'p-1', wikidataQid: 'Q123' });
    const existing = makePerson({ id: 'p-2', wikidataQid: 'Q123', name: 'Different Name' });
    const candidates = findPotentialDuplicatePersons(person, [existing]);
    expect(candidates.length).toBeGreaterThan(0);
    expect(candidates[0].reasons).toContain('Same Wikidata QID');
  });

  test('nearly identical names are a signal', () => {
    const person = makePerson({ id: 'p-1', name: 'Su Shi' });
    const existing = makePerson({ id: 'p-2', name: 'Su Shi', birthYear: 1037 });
    const candidates = findPotentialDuplicatePersons(person, [existing]);
    expect(candidates.length).toBeGreaterThan(0);
  });

  test('different person with no overlap returns empty', () => {
    const person = makePerson({ id: 'p-1', name: 'Su Shi', birthYear: 1037, occupations: ['writer'] });
    const existing = makePerson({
      id: 'p-2',
      name: 'William I',
      alternativeNames: ['William the Conqueror'],
      birthYear: 1028,
      deathYear: 1087,
      regionId: 'england',
      occupations: ['monarch'],
    });
    const candidates = findPotentialDuplicatePersons(person, [existing]);
    // No Wikidata QID match, no name similarity, no region match, no occupation overlap
    // Birth years differ by 9 (within 10) and death years by 14 (outside 2 but within 10)
    // Score should be low
    expect(candidates.length).toBeLessThanOrEqual(1);
    if (candidates.length > 0) {
      expect(candidates[0].score).toBeLessThan(0.5);
    }
  });

  test('skips self', () => {
    const person = makePerson({ id: 'p-1' });
    const candidates = findPotentialDuplicatePersons(person, [person]);
    expect(candidates).toHaveLength(0);
  });
});

describe('findPotentialDuplicateEvents', () => {
  test('same Wikidata QID is strongest signal', () => {
    const event = makeEvent({ id: 'e-1', wikidataQid: 'Q456' });
    const existing = makeEvent({ id: 'e-2', wikidataQid: 'Q456', title: 'Different Title' });
    const candidates = findPotentialDuplicateEvents(event, [existing]);
    expect(candidates.length).toBeGreaterThan(0);
    expect(candidates[0].reasons).toContain('Same Wikidata QID');
  });

  test('similar titles + close years + same region triggers duplicate', () => {
    const event = makeEvent({ id: 'e-1', title: 'Battle of X', startYear: 1070 });
    const existing = makeEvent({ id: 'e-2', title: 'Battle of X', startYear: 1071, regionId: 'test-region' });
    const candidates = findPotentialDuplicateEvents(event, [existing]);
    expect(candidates.length).toBeGreaterThan(0);
  });

  test('unrelated events return empty or low score', () => {
    const event = makeEvent({ id: 'e-1', title: 'Song Dynasty Reform', startYear: 1069, endYear: 1075, regionId: 'china', placeName: 'Kaifeng', tags: ['politics'] });
    const existing = makeEvent({ id: 'e-2', title: 'Norman Conquest', startYear: 1066, endYear: 1066, regionId: 'england', placeName: 'Hastings', tags: ['military'] });
    const candidates = findPotentialDuplicateEvents(event, [existing]);
    // No QID match, no title similarity, no region match, no tag overlap — should be empty or very low score
    expect(candidates.length).toBeLessThanOrEqual(1);
    if (candidates.length > 0) {
      expect(candidates[0].score).toBeLessThan(0.5);
    }
  });

  test('skips self', () => {
    const event = makeEvent({ id: 'e-1' });
    const candidates = findPotentialDuplicateEvents(event, [event]);
    expect(candidates).toHaveLength(0);
  });
});
