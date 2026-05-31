import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Tell turbopack the project root to avoid scanning parent directories
  turbopack: {
    root: process.cwd(),
  },
};

export default nextConfig;
