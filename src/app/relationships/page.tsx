import RelationshipsPageClient from './RelationshipsPageClient';
import { people, regions, personMap, regionMap } from '@/data/mockData';
import { relationships, getAllRelatedPersonIds } from '@/data/relationships';

// Pre-compute related person data on the server
const relatedIds = getAllRelatedPersonIds();
const relatedPeople = new Map<string, typeof people[0]>();
for (const id of relatedIds) {
  const person = personMap.get(id);
  if (person) relatedPeople.set(id, person);
}

export default function RelationshipsPage() {
  return (
    <RelationshipsPageClient
      personMap={relatedPeople}
      regionMap={regionMap}
      relationships={relationships}
    />
  );
}
