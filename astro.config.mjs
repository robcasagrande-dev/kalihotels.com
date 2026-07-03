import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://kalihotels.com',
  trailingSlash: 'always',
  build: {
    format: 'directory'
  },
  integrations: [sitemap()],
  adapter: cloudflare()
});
