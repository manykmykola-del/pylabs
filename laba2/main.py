import math
import re


def series_term(k, a, x):
    return ((-1) ** k) * (x ** (-4 * k)) / (a ** 4 + math.factorial(k))


def partial_sum(limit, a, x):
    total = 0.0
    factorial = 1
    inverse_power = 1.0 / (x ** 4)
    for k in range(1, limit + 1):
        factorial *= k
        total += ((-1) ** k) * (inverse_power ** k) / (a ** 4 + factorial)
    return total


def run_series_task():
    print("\n--- Завдання 1: сума ряду із заданою точністю ---")
    try:
        x = float(input("Введіть x (x ≠ 0): "))
        a = float(input("Введіть a (a ≠ 0): "))
        eps = float(input("Введіть точність ε > 0: "))
    except ValueError:
        print("Помилка: потрібно ввести числові значення.")
        return

    if x == 0 or a == 0:
        print("Помилка: x та a не можуть дорівнювати нулю.")
        return
    if eps <= 0:
        print("Помилка: точність має бути додатною.")
        return

    n = 1
    previous = partial_sum(n, a, x)
    while n < 1_048_576:
        n *= 2
        current = partial_sum(n, a, x)
        if abs(current - previous) < eps:
            print(f"Сума ряду: {current:.10f}")
            print(f"Кількість врахованих доданків: {n}")
            return
        previous = current

    print("Не вдалося досягти заданої точності за прийнятну кількість доданків.")


def run_sequence_task():
    print("\n--- Завдання 2: перший член послідовності із заданою точністю ---")
    try:
        x = float(input("Введіть x (x ≠ 0): "))
        eps = float(input("Введіть точність ε > 0: "))
    except ValueError:
        print("Помилка: потрібно ввести числові значення.")
        return

    if x == 0:
        print("Помилка: x не може дорівнювати нулю.")
        return
    if eps <= 0:
        print("Помилка: точність має бути додатною.")
        return

    previous = x
    try:
        for n in range(1, 101):
            current = (4 / 5) * previous + x / (5 * previous ** 4)
            if abs(current - previous) < eps:
                print(f"Перший знайдений член: a_{n} = {current:.10f}")
                print(f"Його номер у послідовності: {n}")
                print(f"Різниця |a_{n} - a_{n - 1}| = {abs(current - previous):.3e}")
                return
            previous = current
    except ZeroDivisionError:
        print("Помилка: під час обчислень виникло ділення на нуль.")
        return
    except OverflowError:
        print("Помилка: значення вийшло за допустимі межі.")
        return

    print("За перші 100 членів послідовності умову точності не досягнуто.")


def remove_repeated_words(text):
    word_pattern = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*|\d+", re.UNICODE)
    seen = set()
    parts = []
    position = 0

    for match in word_pattern.finditer(text):
        parts.append(text[position:match.start()])
        word = match.group(0)
        key = word.casefold()
        if key not in seen:
            seen.add(key)
            parts.append(word)
        position = match.end()

    parts.append(text[position:])
    result = "".join(parts)
    result = re.sub(r"[ \t]{2,}", " ", result)
    result = re.sub(r"\s+([.,;:!?])", r"\1", result)
    return result.strip()


def run_text_task():
    print("\n--- Завдання 3: вилучення повторних входжень слів ---")
    text = input("Введіть текст: ")
    if not text.strip():
        print("Помилка: текст порожній.")
        return
    print(f"Результат: {remove_repeated_words(text)}")


def decimal_to_binary(number):
    if number < 0:
        return "-" + decimal_to_binary(-number)
    if number < 2:
        return str(number)
    return decimal_to_binary(number // 2) + str(number % 2)


def run_binary_task():
    print("\n--- Завдання 4: рекурсивне переведення у двійкову систему ---")
    try:
        number = int(input("Введіть ціле число n: "))
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return
    print(f"Двійкове подання числа {number}: {decimal_to_binary(number)}")


def show_menu():
    print("\n" + "=" * 54)
    print("Лабораторна робота №2. Варіант 3")
    print("=" * 54)
    print("1. Сума ряду з точністю ε")
    print("2. Перший член послідовності з точністю ε")
    print("3. Вилучити повторні входження слів")
    print("4. Рекурсивне переведення числа у двійкову систему")
    print("0. Вихід")
    print("=" * 54)


def main():
    while True:
        show_menu()
        choice = input("Оберіть пункт меню: ").strip()
        if choice == "1":
            run_series_task()
        elif choice == "2":
            run_sequence_task()
        elif choice == "3":
            run_text_task()
        elif choice == "4":
            run_binary_task()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
