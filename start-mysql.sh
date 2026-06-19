#!/bin/bash
# 启动 MySQL，数据存储在项目目录 mysql_data/（重启不丢失）
mysqld --user=$(whoami) \
  --datadir="$(dirname "$0")/mysql_data" \
  --socket=/tmp/mysql.sock \
  --port=3307 \
  --skip-mysqlx &
sleep 2
mysqladmin ping --socket=/tmp/mysql.sock 2>/dev/null && echo "✅ MySQL is ready" || echo "❌ MySQL failed to start"
