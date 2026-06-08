import { EventPageClient } from './EventPageClient';
import { events, people, regions, personMap, regionMap, eventMap, getPersonsForEvent } from '@/data/mockData';

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

  // Find related events (same region, within 50 years)
  const relatedEventsData = events
    .filter(
      (e) =>
        e.id !== event.id &&
        e.regionId === event.regionId &&
        Math.abs((e.startYear ?? 0) - (event.startYear ?? 0)) <= 50,
    )
    .slice(0, 5)
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
