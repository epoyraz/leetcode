function filter(arr, fn) {
  const result = [];
  for (let i = 0; i < arr.length; i += 1) {
    if (fn(arr[i], i)) {
      result.push(arr[i]);
    }
  }
  return result;
}
