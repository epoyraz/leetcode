import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5

        first, second = (left, right) if philosopher % 2 == 0 else (right, left)
        first_lock = self.forks[first]
        second_lock = self.forks[second]

        with first_lock:
            with second_lock:
                pickLeftFork() if first == left else pickRightFork()
                pickRightFork() if first == left else pickLeftFork()
                eat()
                putRightFork() if first == left else putLeftFork()
                putLeftFork() if first == left else putRightFork()
