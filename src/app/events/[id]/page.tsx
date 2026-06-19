import { EventPageClient } from './EventPageClient';
import {
  findEventById,
  findRegionById,
  findPersonsForEvent,
  findEventsByYearRange,
  findPeopleByIds,
  listRegions,
} from '@/server/db/queries';

const RELATED_EVENT_YEAR_RANGE = 50;
const MAX_RELATED_EVENTS = 5;

interface Props {
  params: Promise<{ id: string }>;
}

export default async function EventPage({ params }: Props) {
  const { id } = await params;
  const event = await findEventById(id);

  if (!event) {
    return <EventPageClient id={id} event={undefined} persons={[]} region={undefined} relatedEvents={[]} />;
  }

  const persons = await findPersonsForEvent(event.id);
  const region = event.regionId ? await findRegionById(event.regionId) : undefined;

  // Find related events (time-range filtered, NOT all events in region)
  const year = event.startYear ?? 0;
  const sameRegionEvents = await findEventsByYearRange(year - RELATED_EVENT_YEAR_RANGE, year + RELATED_EVENT_YEAR_RANGE);
  const relatedSlice = sameRegionEvents
    .filter(e => e.id !== event.id && e.regionId === event.regionId)
    .slice(0, MAX_RELATED_EVENTS);

  // Batch fetch: all related persons + regions in one go
  const allRelatedPersonIds = [...new Set(relatedSlice.flatMap(e => e.personIds))];
  const allRelatedRegionIds = [...new Set(relatedSlice.map(e => e.regionId).filter(Boolean) as string[])];
  const [relatedPersons, allRegions] = await Promise.all([
    allRelatedPersonIds.length ? findPeopleByIds(allRelatedPersonIds) : [],
    allRelatedRegionIds.length ? Promise.all(allRelatedRegionIds.map(id => findRegionById(id))) : [],
  ]);
  const regionMap = new Map(allRegions.filter(Boolean).map(r => [r!.id, r!]));
  const personMap = new Map(relatedPersons.map(p => [p.id, p]));

  const relatedEventsData = relatedSlice.map(e => ({
    event: e,
    region: e.regionId ? regionMap.get(e.regionId) : undefined,
    persons: e.personIds.map(pid => personMap.get(pid)).filter((p): p is NonNullable<typeof p> => p != null),
  }));

  return (
    <EventPageClient id={id} event={event} persons={persons} region={region} relatedEvents={relatedEventsData} />
  );
}
