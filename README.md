# Stopwatch Project

A terminal-based stopwatch application written in Python.

## OOP Enhancements

This project demonstrates several Object-Oriented Programming (OOP) principles:

**1. Inheritance**
- Applied by creating a base class `Timer` and a child class `Stopwatch`.
- Location: `class Stopwatch(Timer)` in `stopwatch.py`.
- Benefit: Allows code reuse and logical organization of timer-related functionality.

**2. Polymorphism**
- Achieved by overriding abstract methods `start` and `stop` in the `Stopwatch` class.
- Location: `def start(self)` and `def stop(self)` in `Stopwatch`.
- Benefit: Enables different timer types to implement their own behaviors while sharing a common interface.

**3. Encapsulation**
- Private attributes (e.g., `__last_elapsed`) and getter/setter methods are used to protect internal state.
- Location: `self.__last_elapsed` and `get_last_elapsed()` in `Stopwatch`.
- Benefit: Prevents direct modification of sensitive data, improving reliability and maintainability.

**4. Abstraction**
- The base class `Timer` is defined as an abstract class with abstract methods.
- Location: `class Timer(ABC)` and `@abstractmethod` decorators in `stopwatch.py`.
- Benefit: Hides implementation details and enforces a contract for subclasses, making the codebase easier to extend and understand.

These enhancements make the project more modular, extensible, and easier to maintain, while providing a clear structure for future improvements.
