/**
 * Wikidata SPARQL client.
 * Handles query execution with timeout, retries, and error handling.
 */

const WIKIDATA_ENDPOINT = 'https://query.wikidata.org/sparql';
const DEFAULT_TIMEOUT_MS = 30000;
const DEFAULT_RETRIES = 3;
const DEFAULT_USER_AGENT = 'HistoricalParallels/1.0 (https://github.com/bryangan-coding/History-Parallel)';

export interface WikidataOptions {
  timeoutMs?: number;
  retries?: number;
  userAgent?: string;
}

interface WikidataResponse {
  head: { vars: string[] };
  results: { bindings: Record<string, { type: string; value: string }>[] };
}

/**
 * Run a SPARQL query against the Wikidata endpoint.
 * Returns parsed JSON response.
 */
export async function runWikidataSparqlQuery(
  query: string,
  options: WikidataOptions = {},
): Promise<WikidataResponse> {
  const {
    timeoutMs = DEFAULT_TIMEOUT_MS,
    retries = DEFAULT_RETRIES,
    userAgent = DEFAULT_USER_AGENT,
  } = options;

  let lastError: Error | undefined;

  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), timeoutMs);

      const url = new URL(WIKIDATA_ENDPOINT);
      url.searchParams.set('format', 'json');
      url.searchParams.set('query', query);

      const response = await fetch(url.toString(), {
        headers: {
          'Accept': 'application/json',
          'User-Agent': userAgent,
        },
        signal: controller.signal,
      });

      clearTimeout(timeout);

      if (!response.ok) {
        const body = await response.text().catch(() => '(no body)');
        throw new Error(
          `Wikidata SPARQL returned HTTP ${response.status}: ${body.substring(0, 200)}`,
        );
      }

      const data = await response.json() as WikidataResponse;

      if (!data.results || !data.results.bindings) {
        throw new Error('Unexpected Wikidata response format');
      }

      return data;
    } catch (error) {
      lastError = error instanceof Error ? error : new Error(String(error));

      if (attempt < retries) {
        const delay = Math.pow(2, attempt) * 1000;
        console.warn(`Wikidata SPARQL attempt ${attempt} failed, retrying in ${delay}ms...`);
        await new Promise((resolve) => setTimeout(resolve, delay));
        continue;
      }

      throw new Error(
        `Wikidata SPARQL query failed after ${retries} attempts: ${lastError.message}`,
      );
    }
  }

  throw lastError ?? new Error('Unknown Wikidata SPARQL error');
}
