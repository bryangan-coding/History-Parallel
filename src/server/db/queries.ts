/**
 * Database queries — now powered by MySQL.
 *
 * All data access uses the MySQL connection pool (src/server/db/mysql.ts).
 * The API signatures match the previous SQLite implementation, so all
 * consumers (server-actions, pages, admin) work without changes.
 *
 * Migrated from Drizzle/SQLite → MySQL on 2026-06-18.
 */
import 'server-only';

export {
  listPeople,
  findPersonById,
  findPeopleByIds,
  listEvents,
  listEventsBySearch,
  listAllEvents,
  findEventById,
  findEventsForPerson,
  findEventsByRegion,
  findEventsByYearRange,
  findPersonsForEvent,
  listRegions,
  findRegionById,
  findSubRegions,
  listSources,
  findSourceById,
  findSourcesForEvent,
  findAllTags,
  updatePersonStatus,
  updateEventStatus,
  updatePersonScore,
  updateEventScore,
} from './mysqlQueries';
