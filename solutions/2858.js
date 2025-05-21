function join(arr1, arr2) {
  const map = new Map();

  // First, add all from arr1
  for (const obj of arr1) {
    map.set(obj.id, { ...obj });
  }

  // Then merge/override with arr2
  for (const obj of arr2) {
    if (map.has(obj.id)) {
      map.set(obj.id, { ...map.get(obj.id), ...obj });
    } else {
      map.set(obj.id, { ...obj });
    }
  }

  // Collect and sort by id
  return Array.from(map.values()).sort((a, b) => a.id - b.id);
}
