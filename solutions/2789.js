function createCounter(init) {
  let value = init;
  return {
    increment: function() {
      value += 1;
      return value;
    },
    decrement: function() {
      value -= 1;
      return value;
    },
    reset: function() {
      value = init;
      return value;
    }
  };
}

// Example Usage:
// const counter = createCounter(5);
// console.log(counter.increment()); // 6
// console.log(counter.reset());     // 5
// console.log(counter.decrement()); // 4
