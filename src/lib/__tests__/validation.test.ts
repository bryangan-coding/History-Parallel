import {
  validatePerson,
  validateHistoricalEvent,
  canPublishPerson,
  canPublishEvent,
} from '../validation';
import type { Person, HistoricalEvent } from '../types';

function makePerson(overrides: Partial<Person> = {}): Person {
  return {
    id: 'test-person',
    name: 'Test Person',
    alternativeNames: [],
    birthYear: 1000,
    deathYear: 1080,
    regionId: 'test-region',
    occupations: ['writer'],
    tags: [],
    summary: 'A test person summary that is long enough.',
    sourceIds: ['src-1'],
    dataStatus: 'published',
    confidenceScore: 0.9,
    externalReferences: [],
    ...overrides,
  };
}

function makeEvent(overrides: Partial<HistoricalEvent> = {}): HistoricalEvent {
  return {
    id: 'test-event',
    title: 'Test Event',
    startYear: 1070,
    datePrecision: 'year',
    isApproximate: false,
    regionId: 'test-region',
    personIds: [],
    tags: [],
    importance: 3,
    summary: 'A test event summary long enough.',
    sourceIds: ['src-1'],
    relatedEventIds: [],
    dataStatus: 'published',
    confidenceScore: 0.9,
    externalReferences: [],
    ...overrides,
  };
}

describe('validatePerson', () => {
  test('empty name is an error', () => {
    const issues = validatePerson(makePerson({ name: '' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'name')).toBe(true);
  });

  test('birthYear after deathYear is an error', () => {
    const issues = validatePerson(makePerson({ birthYear: 1100, deathYear: 1000 }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'birthYear')).toBe(true);
  });

  test('published person without summary is an error', () => {
    const issues = validatePerson(makePerson({ summary: '', dataStatus: 'published' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'summary')).toBe(true);
  });

  test('published person without sources is an error', () => {
    const issues = validatePerson(makePerson({ sourceIds: [], externalReferences: [], dataStatus: 'published' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'sourceIds')).toBe(true);
  });

  test('published person with low confidence is an error', () => {
    const issues = validatePerson(makePerson({ confidenceScore: 0.3, dataStatus: 'published' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'confidenceScore')).toBe(true);
  });

  test('imported person with low confidence is not blocked by confidence check', () => {
    const issues = validatePerson(makePerson({ confidenceScore: 0.3, dataStatus: 'imported' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'confidenceScore')).toBe(false);
  });

  test('valid published person returns no errors', () => {
    const issues = validatePerson(makePerson());
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors).toHaveLength(0);
  });

  test('warns about missing birth year', () => {
    const issues = validatePerson(makePerson({ birthYear: undefined, deathYear: undefined, dataStatus: 'imported' }));
    const warnings = issues.filter((i) => i.level === 'warning');
    expect(warnings.some((w) => w.field === 'birthYear')).toBe(true);
  });
});

describe('validateHistoricalEvent', () => {
  test('empty title is an error', () => {
    const issues = validateHistoricalEvent(makeEvent({ title: '' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'title')).toBe(true);
  });

  test('startYear after endYear is an error', () => {
    const issues = validateHistoricalEvent(makeEvent({ startYear: 1100, endYear: 1000 }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'startYear')).toBe(true);
  });

  test('published event without summary is an error', () => {
    const issues = validateHistoricalEvent(makeEvent({ summary: '', dataStatus: 'published' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'summary')).toBe(true);
  });

  test('published event without sources is an error', () => {
    const issues = validateHistoricalEvent(makeEvent({ sourceIds: [], externalReferences: [], dataStatus: 'published' }));
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors.some((e) => e.field === 'sourceIds')).toBe(true);
  });

  test('warns when event year is outside related person lifespan', () => {
    const person: Person = makePerson({ id: 'p1', name: 'Person A', birthYear: 900, deathYear: 950 });
    const event = makeEvent({ startYear: 1070 });
    const issues = validateHistoricalEvent(event, [person]);
    const warnings = issues.filter((i) => i.level === 'warning');
    expect(warnings.some((w) => w.field === 'startYear')).toBe(true);
  });

  test('valid published event returns no errors', () => {
    const issues = validateHistoricalEvent(makeEvent());
    const errors = issues.filter((i) => i.level === 'error');
    expect(errors).toHaveLength(0);
  });
});

describe('canPublishPerson', () => {
  test('returns ok: false when person has errors', () => {
    const result = canPublishPerson(makePerson({ summary: '', dataStatus: 'published' }));
    expect(result.ok).toBe(false);
  });

  test('returns ok: true for valid person', () => {
    const result = canPublishPerson(makePerson());
    expect(result.ok).toBe(true);
  });
});

describe('canPublishEvent', () => {
  test('returns ok: false when event has errors', () => {
    const result = canPublishEvent(makeEvent({ title: '' }));
    expect(result.ok).toBe(false);
  });

  test('returns ok: true for valid event', () => {
    const result = canPublishEvent(makeEvent());
    expect(result.ok).toBe(true);
  });
});
