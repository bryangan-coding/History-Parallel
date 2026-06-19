import RelationshipsPageClient from './RelationshipsPageClient';
import type { Region } from '@/lib/types';
import { relationships, getAllRelatedPersonIds } from '@/data/relationships';
import { findPeopleByIds, listRegions } from '@/server/db/queries';

export default async function RelationshipsPage() {
  const relatedIds = getAllRelatedPersonIds();
  const [regions, people] = await Promise.all([
    listRegions(),
    findPeopleByIds(relatedIds),
  ]);
  const regionMap = new Map<string, Region>(regions.map((r) => [r.id, r]));

  const relatedPeople = new Map<string, NonNullable<(typeof people)[number]>>();
  for (const p of people) {
    relatedPeople.set(p.id, p);
  }

  return (
    <RelationshipsPageClient
      personMap={relatedPeople}
      regionMap={regionMap}
      relationships={relationships}
    />
  );
}
