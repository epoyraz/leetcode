Array.prototype.snail = function(rowsCount, colsCount) {
  if (rowsCount * colsCount !== this.length) return [];

  const result = Array.from({ length: rowsCount }, () => Array(colsCount).fill(0));
  let i = 0;

  for (let col = 0; col < colsCount; col++) {
    if (col % 2 === 0) {
      for (let row = 0; row < rowsCount; row++) {
        result[row][col] = this[i++];
      }
    } else {
      for (let row = rowsCount - 1; row >= 0; row--) {
        result[row][col] = this[i++];
      }
    }
  }

  return result;
};
