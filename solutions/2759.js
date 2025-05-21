function flat(arr, n) {
  const result = [];

  function helper(subArr, depth) {
    for (const el of subArr) {
      if (Array.isArray(el) && depth < n) {
        helper(el, depth + 1);
      } else {
        result.push(el);
      }
    }
  }

  helper(arr, 0);
  return result;
}
