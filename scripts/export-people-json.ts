/**
 * Export people partitions from mockData.ts to individual JSON files.
 * Run with: npx tsx scripts/export-people-json.ts
 */
import fs from 'fs';
import path from 'path';

// Dynamic import to avoid TypeScript compilation issues with the huge file
async function main() {
  const mockData = await import('../src/data/mockData');

  const partitions: Record<string, any[]> = {
    _peoplePart1: (mockData as any)._peoplePart1 || [],
    _peoplePart2: (mockData as any)._peoplePart2 || [],
    _peoplePart3: (mockData as any)._peoplePart3 || [],
    _peoplePart4: (mockData as any)._peoplePart4 || [],
    _newDynastiesPeople: (mockData as any)._newDynastiesPeople || [],
  };

  const outDir = path.resolve('src/data/people');
  fs.mkdirSync(outDir, { recursive: true });

  for (const [name, data] of Object.entries(partitions)) {
    const outPath = path.join(outDir, `${name}.json`);
    const json = JSON.stringify(data, null, 2);
    fs.writeFileSync(outPath, json, 'utf-8');
    console.log(`✅ ${name}: ${data.length.toLocaleString()} entries → ${outPath} (${fs.statSync(outPath).size.toLocaleString()} bytes)`);
  }

  const total = Object.values(partitions).reduce((sum, arr) => sum + arr.length, 0);
  console.log(`\nTotal: ${total.toLocaleString()} entries across ${Object.keys(partitions).length} files`);
}

main().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});
