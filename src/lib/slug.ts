/**
 * Generate URL-safe slugs from Chinese or mixed-language strings.
 * For people/events/regions, we use the internal ID for routing;
 * this utility can be used for SEO-friendly slugs if needed later.
 */

/**
 * Convert a string to a URL-safe slug.
 * For Chinese characters, we keep them as-is (modern browsers handle them).
 * Replace spaces/punctuation with hyphens.
 */
export function toSlug(text: string): string {
  return text
    .trim()
    .toLowerCase()
    .replace(/[\s，,。；;：:！!？?（）()【】\[\]{}""''、/\\@#$%^&*+=~`|<>]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/-{2,}/g, '-');
}
