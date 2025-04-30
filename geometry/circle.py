import math
from .base import Figure

# Класс, представляющий круг
class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")  # Проверка корректности радиуса
        self.radius = radius

    def area(self) -> float:
        """Вычисление площади круга по формуле: πr²"""
        return math.pi * self.radius ** 2
