function cancellable(gen) {
  let cancelReject;
  let finished = false;

  // A promise that rejects when cancel() is called
  const cancelPromise = new Promise((_, rej) => {
    cancelReject = () => {
      if (!finished) rej("Cancelled");
    };
  });

  // Drive the generator, wiring each yielded promise through Promise.race
  const driver = new Promise((resolve, reject) => {
    function step(nextF, arg) {
      let result;
      try {
        result = nextF.call(gen, arg); // either gen.next(arg) or gen.throw(arg)
      } catch (err) {
        finished = true;
        return reject(err);
      }
      handleResult(result);
    }

    function handleResult({ value, done }) {
      if (done) {
        finished = true;
        return resolve(value);
      }
      // value is assumed to be a Promise
      Promise.race([value, cancelPromise])
        .then(
          v => step(gen.next, v),
          err => {
            if (err === "Cancelled") {
              // inject cancellation into the generator
              try {
                step(gen.throw, "Cancelled");
              } catch (e) {
                finished = true;
                reject(e);
              }
            } else {
              // inject actual error into the generator
              try {
                step(gen.throw, err);
              } catch (e) {
                finished = true;
                reject(e);
              }
            }
          }
        );
    }

    // kick off
    step(gen.next);
  });

  return [
    () => cancelReject(), // the cancel function
    driver               // the promise that resolves/rejects per spec
  ];
}

// -- Example Usage --

// Example 3 from the prompt:
function* tasks() {
  const val = yield new Promise(res => res(2 + 2));
  yield new Promise(res => setTimeout(res, 100));
  return val + 1; // shouldn't execute if cancelled early
}

const [cancel, p] = cancellable(tasks());
setTimeout(cancel, 50);

p.catch(console.log); // logs "Cancelled" at ~50ms
