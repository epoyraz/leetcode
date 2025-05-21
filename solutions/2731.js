function memoize(fn) {
  const cache = new Map();
  let callCount = 0;

  const memoizedFn = (...args) => {
    const key = JSON.stringify(args); // ensures (2,3) â  (3,2)
    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn(...args);
    cache.set(key, result);
    callCount++;
    return result;
  };

  memoizedFn.getCallCount = () => callCount;

  return memoizedFn;
}
