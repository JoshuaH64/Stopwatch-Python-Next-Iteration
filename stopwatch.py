
"""
Stopwatch Application
-----------------------------------
Demonstrates inheritance, polymorphism, encapsulation, and abstraction.

Features:
- Uses abstract base class for timers (abstraction)
- Stopwatch inherits from Timer (inheritance)
- Method overriding (polymorphism)
- Private attributes and getter/setter (encapsulation)
"""

import time
from abc import ABC, abstractmethod

class Timer(ABC):
    def __init__(self):
        self._start_time = None  # protected attribute
        self._end_time = None    # protected attribute

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_elapsed(self):
        if self._start_time is not None and self._end_time is not None:
            return self._end_time - self._start_time
        return 0

class Stopwatch(Timer):
    def __init__(self):
        super().__init__()
        self.__last_elapsed = 0  # private attribute

    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._end_time = time.time()
        self.__last_elapsed = self.get_elapsed()

    def get_last_elapsed(self):
        return self.__last_elapsed

    def reset(self):
        self._start_time = None
        self._end_time = None
        self.__last_elapsed = 0

def main():
    print("\n==============================")
    print("      OOP Stopwatch")
    print("==============================")
    print("Press Enter to start, Enter to stop, and Enter again to reset.")
    print("Type 'q' and press Enter to quit.")
    print("------------------------------")
    sw = Stopwatch()
    while True:
        input("\nPress Enter to start timing...")
        sw.start()
        input("Press Enter to stop timing...")
        sw.stop()
        print(f"Elapsed time: {sw.get_last_elapsed():.2f} seconds")
        print("------------------------------")
        again = input("Press Enter to reset or type 'q' to quit: ")
        if again.lower() == 'q':
            print("Goodbye! Thanks for using the OOP stopwatch.")
            break
        sw.reset()


if __name__ == "__main__":
    main()
    