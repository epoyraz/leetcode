function debounce(fn, t) {
  let timerId = null;

  return function (...args) {
    if (timerId !== null) {
      clearTimeout(timerId);
    }
    timerId = setTimeout(() => {
      fn(...args);
    }, t);
  };
}
