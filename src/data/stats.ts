/**
 * 轻量统计数据 —— 不导入 mockData（避免 117MB JSON 全量加载）
 *
 * 数据来源: src/data/_stats.json（由 scripts/compute-stats.mjs 生成）
 * 数据变更后需重新运行: node scripts/compute-stats.mjs
 */

import _stats from './_stats.json';

export const stats = _stats;
export const totalPeople = _stats.totalPeople;
export const totalEvents = _stats.totalEvents;
export const totalPublished = _stats.totalPublished;
export const peoplePending = _stats.peoplePending;
export const eventsPending = _stats.eventsPending;
export const totalRecords = _stats.totalRecords;
export const totalRegions = _stats.totalRegions;
export const statusCounts = _stats.statusCounts;
export const distribution = _stats.distribution;
export const eraStats = _stats.eraStats;
