import {
  calculatePersonConfidenceScore,
  calculateEventConfidenceScore,
} from '../confidence';
import type { Person, HistoricalEvent, ExternalReference } from '../types';

function makePerson(overrides: Partial<Person> = {}): Person {
  return {
    id: 'p-1',
    name: 'Test Person',
    alternativeNames: [],
    birthYear: 1000,
    deathYear: 1080,
    regionId: 'test-region',
    occupations: ['writer'],
    tags: [],
    summary: 'A test person summary that is more than twenty characters long for scoring.',
    sourceIds: ['src-1'],
    dataStatus: 'imported',
    confidenceScore: 0.5,
    externalReferences: [],
    ...overrides,
  };
}

function makeEvent(overrides: Partial<HistoricalEvent> = {}): HistoricalEvent {
  return {
    id: 'e-1',
    title: 'Test Event',
    startYear: 1070,
    datePrecision: 'year',
    isApproximate: false,
    regionId: 'test-region',
    personIds: ['p-1'],
    tags: [],
    importance: 3,
    summary: 'A test event summary that is more than twenty characters.',
    sourceIds: ['src-1'],
    relatedEventIds: [],
    dataStatus: 'imported',
    confidenceScore: 0.5,
    externalReferences: [],
    ...overrides,
  };
}

describe('calculatePersonConfidenceScore', () => {
  test('returns a number between 0 and 1', () => {
    const score = calculatePersonConfidenceScore(makePerson());
    expect(score).toBeGreaterThanOrEqual(0);
    expect(score).toBeLessThanOrEqual(1);
  });

  test('higher score for person with Wikidata QID', () => {
    const withQid = calculatePersonConfidenceScore(makePerson({ wikidataQid: 'Q123' }));
    const withoutQid = calculatePersonConfidenceScore(makePerson({ wikidataQid: undefined }));
    expect(withQid).toBeGreaterThan(withoutQid);
  });

  test('higher score for person with external references', () => {
    const refs: ExternalReference[] = [
      { id: 'r1', sourceType: 'wikidata', externalId: 'Q1', title: 'test' },
      { id: 'r2', sourceType: 'book', title: 'test book' },
    ];
    const withRefs = calculatePersonConfidenceScore(makePerson({ externalReferences: refs }));
    const withoutRefs = calculatePersonConfidenceScore(makePerson({ externalReferences: [] }));
    expect(withRefs).toBeGreaterThan(withoutRefs);
  });

  test('lower score for person without sources', () => {
    const noSources = calculatePersonConfidenceScore(makePerson({ sourceIds: [], externalReferences: [] }));
    const withSources = calculatePersonConfidenceScore(makePerson({ sourceIds: ['src-1'] }));
    expect(noSources).toBeLessThan(withSources);
  });

  test('lower score for person without birth/death years', () => {
    const noYears = calculatePersonConfidenceScore(makePerson({ birthYear: undefined, deathYear: undefined }));
    const withYears = calculatePersonConfidenceScore(makePerson({ birthYear: 1000, deathYear: 1080 }));
    expect(noYears).toBeLessThan(withYears);
  });

  test('lower score for person without summary', () => {
    const noSummary = calculatePersonConfidenceScore(makePerson({ summary: '' }));
    const withSummary = calculatePersonConfidenceScore(makePerson({ summary: 'A detailed summary of this historical figure with enough text.' }));
    expect(noSummary).toBeLessThan(withSummary);
  });
});

describe('calculateEventConfidenceScore', () => {
  test('returns a number between 0 and 1', () => {
    const score = calculateEventConfidenceScore(makeEvent());
    expect(score).toBeGreaterThanOrEqual(0);
    expect(score).toBeLessThanOrEqual(1);
  });

  test('higher score for event with Wikidata QID', () => {
    const withQid = calculateEventConfidenceScore(makeEvent({ wikidataQid: 'Q456' }));
    const withoutQid = calculateEventConfidenceScore(makeEvent({ wikidataQid: undefined }));
    expect(withQid).toBeGreaterThan(withoutQid);
  });

  test('lower score for event without startYear', () => {
    const noYear = calculateEventConfidenceScore(makeEvent({ startYear: undefined }));
    const withYear = calculateEventConfidenceScore(makeEvent({ startYear: 1070 }));
    expect(noYear).toBeLessThan(withYear);
  });

  test('lower score for event without sources', () => {
    const noSources = calculateEventConfidenceScore(makeEvent({ sourceIds: [], externalReferences: [] }));
    const withSources = calculateEventConfidenceScore(makeEvent({ sourceIds: ['src-1'] }));
    expect(noSources).toBeLessThan(withSources);
  });

  test('lower score for event without summary', () => {
    const noSummary = calculateEventConfidenceScore(makeEvent({ summary: '' }));
    const withSummary = calculateEventConfidenceScore(makeEvent());
    expect(noSummary).toBeLessThan(withSummary);
  });

  test('Wikidata QID alone does not guarantee high score', () => {
    const score = calculateEventConfidenceScore(makeEvent({
      wikidataQid: 'Q456',
      startYear: undefined,
      sourceIds: [],
      externalReferences: [],
      summary: '',
      regionId: undefined,
    }));
    expect(score).toBeLessThan(0.7);
  });
});
