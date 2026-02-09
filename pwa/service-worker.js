// Service Worker 用于离线缓存
const CACHE_NAME = 'buddhist-calendar-v1';
const urlsToCache = [
  './离线佛历万年历工具.html',
  './lunar.js',
  './manifest.json'
];

// 安装 Service Worker
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      })
  );
});

// 拦截请求
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // 如果缓存中有，返回缓存；否则从网络获取
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});

// 激活新的 Service Worker
self.addEventListener('activate', function(event) {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
