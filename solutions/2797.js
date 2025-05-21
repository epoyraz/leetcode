class EventEmitter {
  constructor() {
    this.events = new Map();
  }

  subscribe(event, callback) {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }

    const subscription = { callback };

    this.events.get(event).push(subscription);

    return {
      unsubscribe: () => {
        const subs = this.events.get(event);
        const index = subs.indexOf(subscription);
        if (index !== -1) {
          subs.splice(index, 1);
        }
        if (subs.length === 0) {
          this.events.delete(event);
        }
        return undefined;
      }
    };
  }

  emit(event, args = []) {
    if (!this.events.has(event)) return [];

    const results = [];
    for (const { callback } of this.events.get(event)) {
      results.push(callback(...args));
    }
    return results;
  }
}
