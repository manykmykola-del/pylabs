import math


def calculate_z(x):
    sin_x = math.sin(x)
    return (1 - 2 * sin_x ** 2) / (1 + sin_x ** 2)


def sum_even_numbers(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total


def run_function_value():
    print("\n--- Завдання 1: обчислення значення функції z(x) ---")
    try:
        x = float(input("Введіть x (у радіанах): "))
        z = calculate_z(x)
    except ValueError:
        print("Помилка: потрібно ввести число.")
        return
    except OverflowError:
        print("Помилка: задано занадто велике значення.")
        return
    print(f"z({x}) = {z:.6f}")


def run_even_sum():
    print("\n--- Завдання 2: сума парних чисел від x до y ---")
    try:
        x = int(input("Введіть x: "))
        y = int(input("Введіть y: "))
    except ValueError:
        print("Помилка: потрібно ввести цілі числа.")
        return
    low, high = (x, y) if x <= y else (y, x)
    result = sum_even_numbers(x, y)
    print(f"Сума всіх парних чисел від {low} до {high}: {result}")


def run_array_analysis():
    print("\n--- Завдання 3: аналіз одновимірного масиву ---")
    try:
        size = int(input("Введіть кількість елементів N: "))
    except ValueError:
        print("Помилка: N має бути цілим числом.")
        return
    if size <= 0:
        print("Помилка: кількість елементів має бути додатною.")
        return

    values = []
    while len(values) < size:
        try:
            value = int(input(f"Елемент {len(values) + 1}: "))
        except ValueError:
            print("Помилка: введіть ціле число.")
            continue
        values.append(value)

    print(f"Масив: {values}")

    positive = [value for value in values if value > 0]
    if positive:
        print(f"Мінімальний додатний елемент: {min(positive)}")
    else:
        print("У масиві немає додатних елементів.")

    divisible_by_three = sum(value for value in values if value > 0 and value % 3 == 0)
    print(f"Сума додатних елементів, кратних 3: {divisible_by_three}")

    non_zero = [value for value in values if value != 0]
    print(f"Ненульові елементи: {non_zero}")


def show_menu():
    print("\n" + "=" * 48)
    print("Лабораторна робота №1. Варіант 19")
    print("=" * 48)
    print("1. Обчислити z(x) = (1 - 2sin²x) / (1 + sin²x)")
    print("2. Знайти суму парних чисел від x до y")
    print("3. Обробити одновимірний масив")
    print("0. Вихід")
    print("=" * 48)


def main():
    while True:
        show_menu()
        choice = input("Оберіть пункт меню: ").strip()
        if choice == "1":
            run_function_value()
        elif choice == "2":
            run_even_sum()
        elif choice == "3":
            run_array_analysis()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
