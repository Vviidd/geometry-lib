from typing import Union
from .circle import Circle
from .triangle import Triangle

# Фабричный метод создания фигуры по аргументам
def create_figure(**kwargs) -> Union[Circle, Triangle]:
    if "radius" in kwargs:
        return Circle(kwargs["radius"])  # Создание круга
    elif all(k in kwargs for k in ("a", "b", "c")):
        return Triangle(kwargs["a"], kwargs["b"], kwargs["c"])  # Создание треугольника
    else:
        raise ValueError("Invalid arguments to determine figure type")
