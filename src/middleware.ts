import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware((context, next) => {
  const url = context.url;
  const hostname = url.hostname;
  const pathname = url.pathname.toLowerCase();
  const protoHeader = context.request.headers.get('x-forwarded-proto');

  // Skip redirect/check on local development
  if (hostname === 'localhost' || hostname === '127.0.0.1' || hostname.endsWith('.local')) {
    return next();
  }

  // 1. Purge legacy WordPress & PHP endpoints (Return 410 Gone)
  const isLegacyWp =
    pathname.startsWith('/wp-content/') ||
    pathname.startsWith('/wp-includes/') ||
    pathname.startsWith('/wp-admin/') ||
    pathname.startsWith('/wp-json/') ||
    pathname.startsWith('/wp-login') ||
    pathname.endsWith('.php') ||
    pathname.startsWith('/author/') ||
    pathname.startsWith('/category/') ||
    pathname.startsWith('/tag/') ||
    pathname.startsWith('/feed/');

  if (isLegacyWp) {
    return new Response('410 Gone - Legacy WordPress endpoint no longer exists on this Astro site.', {
      status: 410,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' }
    });
  }

  // 2. Force HTTPS and Non-WWW
  const isHttp = protoHeader === 'http' || url.protocol === 'http:';
  const isWww = hostname.startsWith('www.');

  if (isHttp || isWww) {
    const targetUrl = new URL(url.pathname + url.search, 'https://kalihotels.com');
    return context.redirect(targetUrl.toString(), 301);
  }

  return next();
});
