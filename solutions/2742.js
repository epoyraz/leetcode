Array.prototype.groupBy = function(fn) {
  const result = {};
  for (const item of this) {
    const key = fn(item);
    if (!result.hasOwnProperty(key)) {
      result[key] = [];
    }
    result[key].push(item);
  }
  return result;
};

// Example Usage:
// const array = [{ id: '1' }, { id: '1' }, { id: '2' }];
// const grouped = array.groupBy(item => item.id);
// console.log(grouped);
// // { '1': [{ id: '1' }, { id: '1' }], '2': [{ id: '2' }] }
