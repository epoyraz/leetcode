function checkIfInstanceOf(val, cls) {
  // cls must be a constructor function
  if (typeof cls !== 'function') return false;
  // null/undefined canât be instances of anything
  if (val == null) return false;

  // Box primitives so that, e.g., 5 â Number(5), and still treat functions/objects as is
  const wrapped = (typeof val !== 'object' && typeof val !== 'function')
    ? Object(val)
    : val;

  // Rely on JavaScriptâs instanceof to check the prototype chain
  return wrapped instanceof cls;
}
