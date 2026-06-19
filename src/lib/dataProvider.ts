/**
 * Data Provider — 历史平行线 (History Parallel) 数据访问
 *
 * 所有数据通过 MySQL 连接池访问。数据已从 JSON 文件迁移到 MySQL 数据库，
 * 不再需要 mock data fallback。
 *
 * 架构：页面/组件 → @/server/db/queries → MySQL
 *
 * 本文件提供 MySQLDataProvider 的懒加载单例，供需要 DataProvider 接口的代码使用。
 * 大部分页面直接使用 @/server/db/queries 中的函数，不需要通过本文件。
 */
import type { DataProvider } from './dataProviderTypes';

// ============================================================
// MySQLDataProvider — 懒加载，仅服务端，并发安全
// ============================================================

let mysqlProvider: DataProvider | null = null;
let mysqlProviderPromise: Promise<DataProvider> | null = null;

async function getMySQLProvider(): Promise<DataProvider> {
  if (mysqlProvider) return mysqlProvider;
  if (mysqlProviderPromise) return mysqlProviderPromise;

  mysqlProviderPromise = import('@/server/db/MySQLDataProvider').then(mod => {
    mysqlProvider = new mod.MySQLDataProvider();
    return mysqlProvider;
  });
  return mysqlProviderPromise;
}

const activeProvider: Promise<DataProvider> = getMySQLProvider();

/** Resolve the MySQL provider (handles async lazy-loading) */
export async function resolveProvider(): Promise<DataProvider> {
  return activeProvider;
}

export default activeProvider;
