import { PersonPageClient } from './PersonPageClient';
import type { Region } from '@/lib/types';
import {
  findPersonById,
  findRegionById,
  findEventsForPerson,
} from '@/server/db/queries';

interface Props {
  params: Promise<{ id: string }>;
}

export default async function PersonPage({ params }: Props) {
  const { id } = await params;
  const person = await findPersonById(id);

  if (!person) {
    return <PersonPageClient id={id} person={undefined} region={undefined} personEvents={[]} eventRegions={new Map()} />;
  }

  const region = person.regionId ? await findRegionById(person.regionId) : undefined;
  const personEvents = await findEventsForPerson(person.id);

  // Batch fetch all event regions (no N+1)
  const regionIds = [...new Set(personEvents.map(e => e.regionId).filter(Boolean) as string[])];
  const regions = regionIds.length > 0
    ? await Promise.all(regionIds.map(id => findRegionById(id)))
    : [];
  const regionLookup = new Map(regions.filter(Boolean).map(r => [r!.id, r]));

  const eventRegions = new Map<string, Region | undefined>();
  for (const e of personEvents) {
    eventRegions.set(e.id, e.regionId ? regionLookup.get(e.regionId) : undefined);
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
