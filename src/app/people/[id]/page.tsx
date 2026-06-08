import { PersonPageClient } from './PersonPageClient';
import { people, events, regions, personMap, regionMap, getEventsForPerson } from '@/data/mockData';
import type { Region } from '@/lib/types';

interface Props {
  params: Promise<{ id: string }>;
}

export default async function PersonPage({ params }: Props) {
  const { id } = await params;
  const person = personMap.get(id);

  if (!person) {
    return <PersonPageClient id={id} person={undefined} region={undefined} personEvents={[]} eventRegions={new Map()} />;
  }

  // Pre-resolve all data on the server
  const region = person.regionId ? regionMap.get(person.regionId) : undefined;
  const personEvents = getEventsForPerson(person.id);

  // Pre-resolve regions for each event (for the Timeline component)
  const eventRegions = new Map<string, Region | undefined>();
  for (const e of personEvents) {
    eventRegions.set(e.id, e.regionId ? regionMap.get(e.regionId) : undefined);
  }

  return (
    <PersonPageClient
      id={id}
      person={person}
      region={region}
      personEvents={personEvents}
      eventRegions={eventRegions}
    />
  );
}
