/**
 * DataProvider interface type — 独立类型文件，避免循环依赖
 */
import type {
  Region,
  Person,
  HistoricalEvent,
  Source,
  ParallelRegionGroup,
  TimeRange,
} from './types';

export interface DataProvider {
  // ---- Regions ----
  getRegions(): Promise<Region[]>;
  getRegionById(id: string): Promise<Region | undefined>;

  // ---- Persons ----
  getPersons(): Promise<Person[]>;
  getPersonById(id: string): Promise<Person | undefined>;
  getPersonsForEvent(eventId: string): Promise<Person[]>;

  // ---- Events ----
  getEvents(): Promise<HistoricalEvent[]>;
  getEventById(id: string): Promise<HistoricalEvent | undefined>;
  getEventsForPerson(personId: string): Promise<HistoricalEvent[]>;
  getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]>;

  // ---- Sources ----
  getSources(): Promise<Source[]>;
  getSourceById(id: string): Promise<Source | undefined>;
  getSourcesForEvent(eventId: string): Promise<Source[]>;

  // ---- Search ----
  search(query: string): Promise<{
    people: Person[];
    events: HistoricalEvent[];
    regions: Region[];
    yearMatches: { year: number; nearEvents: HistoricalEvent[]; label: string }[];
  }>;

  // ---- Parallel events ----
  getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]>;
}
