/**
 * Wikidata SPARQL query builders.
 * Pre-built SPARQL query templates for common historical data retrieval.
 */

/**
 * Build a SPARQL query to fetch historical persons from Wikidata.
 */
export function buildPersonQuery(params: {
  birthYearStart?: number;
  birthYearEnd?: number;
  region?: string;
  occupation?: string;
  limit?: number;
}): string {
  const { birthYearStart, birthYearEnd, region, occupation, limit = 50 } = params;

  let filters = '';

  // Year filters
  if (birthYearStart && birthYearEnd) {
    filters += `
  FILTER(YEAR(?birthDate) >= ${birthYearStart} && YEAR(?birthDate) <= ${birthYearEnd})\n`;
  } else if (birthYearStart) {
    filters += `  FILTER(YEAR(?birthDate) >= ${birthYearStart})\n`;
  } else if (birthYearEnd) {
    filters += `  FILTER(YEAR(?birthDate) <= ${birthYearEnd})\n`;
  }

  // Occupation filter
  if (occupation) {
    filters += `  ?person wdt:P106 wd:${occupation} .\n`;
  }

  return `
SELECT DISTINCT ?person ?personLabel ?birthDate ?deathDate ?occupationLabel
WHERE {
  ?person wdt:P31 wd:Q5 .
  ?person wdt:P569 ?birthDate .
  OPTIONAL { ?person wdt:P570 ?deathDate . }
  OPTIONAL { ?person wdt:P106 ?occupation . }
${filters}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,zh". }
}
ORDER BY ?birthDate
LIMIT ${limit}
`;
}

/**
 * Build a SPARQL query to fetch historical events from Wikidata.
 */
export function buildEventQuery(params: {
  startYear?: number;
  endYear?: number;
  region?: string;
  tag?: string;
  limit?: number;
}): string {
  const { startYear, endYear, limit = 100 } = params;

  let filters = '';

  if (startYear) {
    filters += `  FILTER(YEAR(?pointInTime) >= ${startYear})\n`;
  }
  if (endYear) {
    filters += `  FILTER(YEAR(?pointInTime) <= ${endYear})\n`;
  }

  return `
SELECT DISTINCT ?event ?eventLabel ?pointInTime ?placeLabel
WHERE {
  ?event wdt:P31/wdt:P279* wd:Q1190554 .
  ?event wdt:P585 ?pointInTime .
  OPTIONAL { ?event wdt:P276 ?place . }
${filters}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,zh". }
}
ORDER BY ?pointInTime
LIMIT ${limit}
`;
}
