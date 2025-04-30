from geometry.factory import create_figure

# Создаем круг радиуса 2
circle = create_figure(radius=2)
print(f"Площадь круга: {circle.area():.2f}")

# Создаем треугольник со сторонами 3, 4, 5
triangle = create_figure(a=3, b=4, c=5)
print(f"Площадь треугольника: {triangle.area():.2f}")
print(f"Это прямоугольный треугольник? {'Да' if triangle.is_right() else 'Нет'}")