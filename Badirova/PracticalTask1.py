import math


def is_valid_triangle(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                return True
    return False


def get_triangle_type_1(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Неверные длины сторон треугольника", None

    try:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    except ValueError:
        return "Невозможно вычислить площадь", None

    if a != b and b != c and a != c:
        return 'разносторонний', area
    elif a == b == c:
        return 'равносторонний', area
    else:
        return 'равнобедренный', area


def get_triangle_type_2(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Неверные длины сторон треугольника", None

    try:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        angles = sorted([a, b, c])
        if angles[0] ** 2 + angles[1] ** 2 > angles[2] ** 2:
            return 'остроугольный', area
        elif angles[0] ** 2 + angles[1] ** 2 < angles[2] ** 2:
            return 'тупоугольный', area
        else:
            return 'прямоугольный', area
    except ValueError:
        return "Невозможно вычислить площадь", None


test_cases_1 = [
    (6.0, 8.0, 10.0, 'разносторонний'),
    (7.0, 7.0, 7.0, 'равносторонний'),
    (5.0, 5.0, 7.0, 'равнобедренный'),
    (0.0, 4.0, 5.0, 'ошибка'),
    (4.0, 0.0, 5.0, 'ошибка'),
    (4.0, 5.0, 0.0, 'ошибка'),
    (-4.0, 5.0, 5.0, 'ошибка'),
    (4.0, -5.0, 5.0, 'ошибка'),
    (4.0, 5.0, -5.0, 'ошибка'),
    ("a", 4.0, 5.0, 'ошибка'),
    (4.0, "b", 5.0, 'ошибка'),
    (4.0, 5.0, "c", 'ошибка')
]

test_cases_2 = [
    (3.0, 4.0, 5.0, 'прямоугольный'),
    (5.0, 5.0, 6.0, 'остроугольный'),
    (4.0, 4.0, 7.0, 'тупоугольный'),
    (0.0, 4.0, 5.0, 'ошибка'),
    (4.0, 0.0, 5.0, 'ошибка'),
    (4.0, 5.0, 0.0, 'ошибка'),
    (-4.0, 5.0, 5.0, 'ошибка'),
    (4.0, -5.0, 5.0, 'ошибка'),
    (4.0, 5.0, -5.0, 'ошибка'),
    ("a", 4.0, 5.0, 'ошибка'),
    (4.0, "b", 5.0, 'ошибка'),
    (4.0, 5.0, "c", 'ошибка')
]

print("Задание 1-2 практической работы №1,2:")
print("A   |   B   |   C   | Ожидаемый результат: | Результат теста:")
for a, b, c, expected_result in test_cases_1:
    try:
        result = get_triangle_type_1(a, b, c)
        print(f"a={a}, b={b}, c={c} | {expected_result} | {result}")
    except:
        print("Введите числовые значения")

print("Задание 3-4 практической работы №1,2:")
print("A   |   B   |   C   | Ожидаемый результат: | Результат теста:")
for a, b, c, expected_result in test_cases_2:
    try:
        result = get_triangle_type_2(a, b, c)
        print(f"a={a}, b={b}, c={c} | {expected_result} | {result}")
    except:
        print("Введите числовые значения")
