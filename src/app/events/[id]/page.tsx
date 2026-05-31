import { EventPageClient } from './EventPageClient';

interface Props {
  params: Promise<{ id: string }>;
}

export default async function EventPage({ params }: Props) {
  const { id } = await params;
  return <EventPageClient id={id} />;
}
