const CACHE_NAME = 'carrie-desk-v1';
const ASSETS = [
  '/carrie-desk/',
  '/carrie-desk/index.html',
  '/carrie-desk/manifest.json',
  '/carrie-desk/icon-192.png',
  '/carrie-desk/icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  if (event.request.mode === 'navigate') {
    event.respondWith(
      caches.match('/carrie-desk/index.html').then(response => {
        return response || fetch(event.request);
      })
    );
  }
});
