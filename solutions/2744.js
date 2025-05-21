function memoize(fn) {
  // A unique symbol to store results at a leaf
  const RESULT = Symbol('result');
  // Nested Maps: each level maps an argument â next Map (or finally a stored result)
  const cache = new Map();
  let callCount = 0;

  function memoized(...args) {
    let node = cache;
    // Traverse/extend the nested Map structure for each argument
    for (const arg of args) {
      if (!node.has(arg)) {
        node.set(arg, new Map());
      }
      node = node.get(arg);
    }
    // Now `node` is the leaf-map for this exact args tuple
    if (node.has(RESULT)) {
      // cache-hit
      return node.get(RESULT);
    }
    // cache-miss â call original, store result
    const value = fn(...args);
    callCount++;
    node.set(RESULT, value);
    return value;
  }

  // Expose a method to read how many real calls were made
  memoized.getCallCount = () => callCount;
  return memoized;
}
