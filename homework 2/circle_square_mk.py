import random

def circle_square_mk(r, n):
    points_inside_circle = 0

    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        if x**2 + y**2 <= r**2:
            points_inside_circle += 1

    square = 4 * r**2 * (points_inside_circle / n)
    return square

# Проверка функции
if __name__ == "__main__":
    radius = 1
    num_experiments = 1000000

    # Вычисление площади окружности по формуле
    true_square = 3.141592653589793 * radius**2

    # Вычисление площади окружности методом Монте-Карло
    monte_carlo_square = circle_square_mk(radius, num_experiments)

    print("Площадь окружности по формуле:", true_square)
    print("Площадь окружности методом Монте-Карло ({} экспериментов):".format(num_experiments), monte_carlo_square)