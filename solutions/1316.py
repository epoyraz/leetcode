import threading

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.cond = threading.Condition()

    def fizz(self, printFizz):
        while True:
            with self.cond:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cond.wait()
                if self.current > self.n:
                    self.cond.notify_all()
                    return
                printFizz()
                self.current += 1
                self.cond.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.cond:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cond.wait()
                if self.current > self.n:
                    self.cond.notify_all()
                    return
                printBuzz()
                self.current += 1
                self.cond.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cond:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 != 0):
                    self.cond.wait()
                if self.current > self.n:
                    self.cond.notify_all()
                    return
                printFizzBuzz()
                self.current += 1
                self.cond.notify_all()

    def number(self, printNumber):
        while True:
            with self.cond:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cond.wait()
                if self.current > self.n:
                    self.cond.notify_all()
                    return
                printNumber(self.current)
                self.current += 1
                self.cond.notify_all()
