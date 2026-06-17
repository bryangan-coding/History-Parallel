/**
 * 共享时代边界定义 —— 同时供 API route 和 stats 脚本使用。
 *
 * 约定：下限含（>=），上限不含（<），与 Python range 语义一致。
 * 这样相邻区间无重叠，且每个出生年份唯一归属一个时代。
 *
 * 如果修改了此文件，需同步运行：
 *   node scripts/compute-stats.mjs
 *   → 重新生成 src/data/_stats.json
 */

export const ERAS = [
  {
    key: 'ancient',
    label: '公元前',
    labelEn: 'BCE',
    min: -3000,
    max: 0,         // birthYear < 0
  },
  {
    key: 'earlyMedieval',
    label: '1–10 世纪',
    labelEn: '1st–10th Century',
    min: 1,
    max: 960,       // 1 <= birthYear < 960
  },
  {
    key: 'song',
    label: '宋（960–1278）',
    labelEn: 'Song (960–1278)',
    min: 960,
    max: 1279,      // 960 <= birthYear < 1279
  },
  {
    key: 'postSong',
    label: '宋后–明（1279–1499）',
    labelEn: 'Post-Song to Ming (1279–1499)',
    min: 1279,
    max: 1500,      // 1279 <= birthYear < 1500
  },
  {
    key: 'modern',
    label: '1500 年后',
    labelEn: 'After 1500',
    min: 1500,
    max: null,        // birthYear >= 1500（无上限）
  },
];
