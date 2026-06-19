/**
 * MySQL connection pool for history_parallel database
 * Used by MySQLDataProvider for server-side data access
 */
import mysql from 'mysql2/promise';

const pool = mysql.createPool({
  host: process.env.MYSQL_HOST || 'localhost',
  port: parseInt(process.env.MYSQL_PORT || '3307', 10),
  user: process.env.MYSQL_USER || 'root',
  password: process.env.MYSQL_PASSWORD ?? undefined,
  database: process.env.MYSQL_DATABASE || 'history_parallel',
  charset: 'utf8mb4',
  socketPath: process.env.MYSQL_SOCKET || '/tmp/mysql.sock',
  waitForConnections: true,
  connectionLimit: 10,
  maxIdle: 5,
  idleTimeout: 60000,
  queueLimit: 0,
  enableKeepAlive: true,
  keepAliveInitialDelay: 10000,
});

export default pool;

/**
 * Helper: parse a MySQL JSON column to an array
 */
export function parseJsonArray(value: unknown, defaultVal: string[] = []): string[] {
  if (!value) return defaultVal;
  if (Array.isArray(value)) return value as string[];
  try {
    const parsed = JSON.parse(value as string);
    return Array.isArray(parsed) ? parsed : defaultVal;
  } catch {
    return defaultVal;
  }
}

/**
 * Helper: parse MySQL JSON column to an object
 */
export function parseJsonObject(value: unknown, defaultVal: Record<string, unknown> | null = null): Record<string, unknown> | null {
  if (!value) return defaultVal;
  if (typeof value === 'object' && !Array.isArray(value)) return value as Record<string, unknown>;
  try {
    return JSON.parse(value as string);
  } catch {
    return defaultVal;
  }
}
