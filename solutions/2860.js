/**
 * @param {any[]} arr
 * @param {function(any): number} fn
 * @return {any[]}
 */
function sortBy(arr, fn) {
  // Decorate: pair each element with its key
  const paired = arr.map(item => ({ key: fn(item), value: item }));
  // Sort by the computed key
  paired.sort((a, b) => a.key - b.key);
  // Undecorate: extract the original items in sorted order
  return paired.map(pair => pair.value);
}
