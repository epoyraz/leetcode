class TimeLimitedCache {
  constructor() {
    this.cache = new Map(); // key -> { value, expiresAt }
  }

  set(key, value, duration) {
    const now = Date.now();
    const exists = this.cache.has(key) && this.cache.get(key).expiresAt > now;

    // Set/overwrite key with new value and expiration time
    this.cache.set(key, {
      value,
      expiresAt: now + duration
    });

    return exists;
  }

  get(key) {
    const now = Date.now();
    if (this.cache.has(key)) {
      const entry = this.cache.get(key);
      if (entry.expiresAt > now) {
        return entry.value;
      } else {
        this.cache.delete(key); // Clean up expired key
      }
    }
    return -1;
  }

  count() {
    const now = Date.now();
    let count = 0;
    for (const [key, { expiresAt }] of this.cache.entries()) {
      if (expiresAt > now) {
        count++;
      } else {
        this.cache.delete(key); // Optionally clean up expired entries
      }
    }
    return count;
  }
}
