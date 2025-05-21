function* inorderTraversal(arr) {
  for (const item of arr) {
    if (Array.isArray(item)) {
      // Recurse into sub-array
      yield* inorderTraversal(item);
    } else {
      // Yield integer
      yield item;
    }
  }
}