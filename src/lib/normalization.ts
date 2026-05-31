/**
 * Data normalization utilities.
 * Standardizes imported data before it enters the review pipeline.
 */

import type { ExternalReference } from './types';

/**
 * Normalize a person's name: trim whitespace, normalize spacing.
 * Does NOT modify case for Chinese names.
 */
export function normalizePersonName(name: string): string {
  if (!name) return '';
  return name
    .trim()
    .replace(/\s+/g, ' ')
    .replace(/[\u00A0\u3000]/g, ' '); // Replace non-breaking spaces
}

/**
 * Normalize an event title: trim whitespace, normalize spacing.
 */
export function normalizeEventTitle(title: string): string {
  if (!title) return '';
  return title
    .trim()
    .replace(/\s+/g, ' ')
    .replace(/[\u00A0\u3000]/g, ' ');
}

/**
 * Normalize a region name.
 */
export function normalizeRegionName(name: string): string {
  if (!name) return '';
  return name.trim().replace(/\s+/g, ' ');
}

/**
 * Normalize tags: trim, deduplicate, filter empty, sort alphabetically.
 */
export function normalizeTags(tags: string[]): string[] {
  if (!tags || tags.length === 0) return [];

  return [...new Set(
    tags
      .map((t) => t.trim().replace(/\s+/g, ' '))
      .filter((t) => t.length > 0),
  )].sort();
}

/**
 * Normalize an external reference: ensure required fields, trim strings.
 */
export function normalizeExternalReference(reference: ExternalReference): ExternalReference {
  return {
    ...reference,
    title: reference.title?.trim(),
    author: reference.author?.trim(),
    publisher: reference.publisher?.trim(),
    url: reference.url?.trim(),
    license: reference.license?.trim(),
    note: reference.note?.trim(),
  };
}

/**
 * Create a URL-safe slug from a string.
 * Supports both English and Chinese text.
 */
export function createSlug(input: string): string {
  if (!input) return '';

  // For English-heavy text: lowercase and replace non-alphanumeric
  // For mixed text: just strip special characters and normalize
  return input
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 80);
}
