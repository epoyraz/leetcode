function promiseAll(functions) {
  return new Promise((resolve, reject) => {
    const n = functions.length;
    const results = new Array(n);
    let count = 0;
    let hasRejected = false;

    functions.forEach((fn, i) => {
      // Execute each function immediately
      Promise.resolve()
        .then(fn)
        .then(value => {
          if (hasRejected) return;
          results[i] = value;
          count += 1;
          if (count === n) {
            resolve(results);
          }
        })
        .catch(err => {
          if (!hasRejected) {
            hasRejected = true;
            reject(err);
          }
        });
    });
  });
}
