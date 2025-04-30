import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.factory import create_figure
import math
import pytest

def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)

def test_factory_circle():
    fig = create_figure(radius=2)
    assert isinstance(fig, Circle)
    assert math.isclose(fig.area(), math.pi * 4)

def test_factory_triangle():
    fig = create_figure(a=3, b=4, c=5)
    assert isinstance(fig, Triangle)
    assert fig.is_right()
