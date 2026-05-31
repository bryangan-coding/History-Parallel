// Server-only data arrays
// This file contains the LARGE data arrays that should NOT be inlined in client bundles
// Client components should use server actions (server-actions.ts) to access this data

import 'server-only';

// Re-export everything from mockData.ts — but this file is marked server-only
// so the data will only be available on the server
export {
  people,
  events,
  regions,
  sources,
} from './mockData';

export {
  getPersonById,
  getEventById,
  getRegionById,
  getSubRegions,
  getEventsByRegion,
  getSourcesForEvent,
  getPersonsForEvent,
  getEventsForPerson,
  getAllTags,
} from './mockData';
