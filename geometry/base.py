from abc import ABC, abstractmethod

# Абстрактный базовый класс для всех геометрических фигур
class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        """Метод для вычисления площади фигуры"""
        pass
