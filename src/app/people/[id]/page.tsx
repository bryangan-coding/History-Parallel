import { PersonPageClient } from './PersonPageClient';

interface Props {
  params: Promise<{ id: string }>;
}

export default async function PersonPage({ params }: Props) {
  const { id } = await params;
  return <PersonPageClient id={id} />;
}
