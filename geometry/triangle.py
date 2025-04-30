import math
from .base import Figure

# Класс, представляющий треугольник
class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        # Проверка на положительность сторон
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Sides must be positive")
        # Проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        """Вычисление площади по формуле Герона"""
        s = (self.a + self.b + self.c) / 2  # Полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """Проверка, является ли треугольник прямоугольным по теореме Пифагора"""
        sides = sorted([self.a, self.b, self.c])  # Отсортировать стороны по длине
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
