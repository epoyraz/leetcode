Function.prototype.callPolyfill = function(obj, ...args) {
  // Use a Symbol to avoid property name collision
  const tempKey = Symbol();
  obj[tempKey] = this;       // Attach the function to obj
  const result = obj[tempKey](...args); // Call it with args
  delete obj[tempKey];       // Clean up
  return result;
};
