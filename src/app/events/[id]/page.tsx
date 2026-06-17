import { EventPageClient } from './EventPageClient';
import { events, people, regions, personMap, regionMap, eventMap, getPersonsForEvent } from '@/data/mockData';

const RELATED_EVENT_YEAR_RANGE = 50;
const MAX_RELATED_EVENTS = 5;

interface Props {
  params: Promise<{ id: string }>;
}

export default async function EventPage({ params }: Props) {
  const { id } = await params;
  const event = eventMap.get(id);

  if (!event) {
    return <EventPageClient id={id} event={undefined} persons={[]} region={undefined} relatedEvents={[]} />;
  }

  // Pre-resolve all data on the server
  const persons = getPersonsForEvent(event.id);
  const region = event.regionId ? regionMap.get(event.regionId) : undefined;

  // Find related events (same region, within RELATED_EVENT_YEAR_RANGE years)
  const relatedEventsData = events
    .filter(
      (e) =>
        e.id !== event.id &&
        e.regionId === event.regionId &&
        Math.abs((e.startYear ?? 0) - (event.startYear ?? 0)) <= RELATED_EVENT_YEAR_RANGE,
    )
    .slice(0, MAX_RELATED_EVENTS)
    .map((e) => ({
      event: e,
      region: e.regionId ? regionMap.get(e.regionId) : undefined,
      persons: getPersonsForEvent(e.id),
    }));

  return (
    <EventPageClient
      id={id}
      event={event}
      persons={persons}
      region={region}
      relatedEvents={relatedEventsData}
    />
  );
}
