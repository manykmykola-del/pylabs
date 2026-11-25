def count_distinct(values):
    return len(set(values))


def build_distinct_vector(matrix):
    return [count_distinct(row) for row in matrix]


def print_vector(vector, per_line=10):
    for start in range(0, len(vector), per_line):
        chunk = vector[start:start + per_line]
        print(" ".join(f"{value:3d}" for value in chunk))


def run_matrix_task():
    print("\n--- Завдання 1: кількість різних елементів у рядках матриці ---")
    try:
        n = int(input("Введіть розмірність матриці n (1 ≤ n ≤ 20): "))
    except ValueError:
        print("Помилка: n має бути цілим числом.")
        return
    if not (1 <= n <= 20):
        print("Помилка: n має бути в межах від 1 до 20.")
        return

    matrix = []
    for row_index in range(n):
        while True:
            raw = input(f"Рядок {row_index + 1} ({n} цілих чисел): ").strip().split()
            if len(raw) != n:
                print(f"Потрібно ввести рівно {n} чисел.")
                continue
            try:
                row = [int(value) for value in raw]
            except ValueError:
                print("Помилка: усі елементи рядка мають бути цілими числами.")
                continue
            matrix.append(row)
            break

    print("\nВведена матриця:")
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))

    vector = build_distinct_vector(matrix)
    print("\nВектор B (кількість різних елементів у кожному рядку):")
    print_vector(vector)


def average_height_by_gender(records, gender):
    heights = [height for height, person_gender in records if person_gender == gender]
    if not heights:
        return None, 0
    return sum(heights) / len(heights), len(heights)


def run_height_task():
    print("\n--- Завдання 2: середній зріст чоловіків ---")
    try:
        n = int(input("Введіть кількість осіб (за умовою 20): "))
    except ValueError:
        print("Помилка: кількість осіб має бути цілим числом.")
        return
    if n <= 0:
        print("Помилка: кількість осіб має бути додатною.")
        return

    records = []
    print("Вводьте дані у форматі: <зріст> <стать>, де стать — M/Ч або F/Ж.")
    for index in range(n):
        while True:
            parts = input(f"Особа {index + 1}: ").strip().split()
            if len(parts) != 2:
                print("Потрібно ввести два значення: зріст і стать.")
                continue
            try:
                height = float(parts[0])
            except ValueError:
                print("Помилка: зріст має бути числом.")
                continue
            gender = parts[1].upper()
            if gender in {"M", "Ч", "CH"}:
                gender = "M"
            elif gender in {"F", "Ж"}:
                gender = "F"
            else:
                print("Помилка: стать має бути M/Ч або F/Ж.")
                continue
            if height <= 0:
                print("Помилка: зріст має бути додатним.")
                continue
            records.append((height, gender))
            break

    average, count = average_height_by_gender(records, "M")
    if average is None:
        print("У вибірці немає чоловіків.")
    else:
        print(f"Середній зріст чоловіків: {average:.2f} см (кількість: {count})")


def count_strike_days(days_in_year, schedules):
    strike_days = set()
    for start_day, period in schedules:
        for day in range(start_day, days_in_year + 1, period):
            if day % 7 not in (6, 0):
                strike_days.add(day)
    return len(strike_days)


def run_strikes_task():
    print("\n--- Завдання 3: загальнонаціональні страйки ---")
    while True:
        header = input("Введіть кількість днів N та кількість партій K (через пробіл): ").strip().split()
        if len(header) != 2:
            print("Помилка: потрібно ввести два цілих числа N і K.")
            continue
        try:
            days_in_year = int(header[0])
            parties_count = int(header[1])
        except ValueError:
            print("Помилка: N та K мають бути цілими числами.")
            continue
        if not (1 < days_in_year < 1_000_000) or not (1 < parties_count < 100):
            print("Помилка: мають виконуватися умови 1 < N < 1000000 та 1 < K < 100.")
            continue
        break

    schedules = []
    for index in range(parties_count):
        while True:
            parts = input(f"Партія {index + 1} (a_i b_i): ").strip().split()
            if len(parts) != 2:
                print("Потрібно ввести два цілих числа: a_i та b_i.")
                continue
            try:
                start_day = int(parts[0])
                period = int(parts[1])
            except ValueError:
                print("Помилка: a_i та b_i мають бути цілими числами.")
                continue
            if not (1 <= start_day <= days_in_year) or period <= 0:
                print("Помилка: некоректні значення дня початку або періоду.")
                continue
            schedules.append((start_day, period))
            break

    total_strikes = count_strike_days(days_in_year, schedules)
    print(f"\nКількість страйків протягом року: {total_strikes}")


def show_menu():
    print("\n" + "=" * 56)
    print("Лабораторна робота №3. Варіант 6")
    print("=" * 56)
    print("1. Кількість різних елементів у рядках матриці")
    print("2. Середній зріст чоловіків")
    print("3. Загальнонаціональні страйки")
    print("0. Вихід")
    print("=" * 56)


def main():
    while True:
        show_menu()
        choice = input("Оберіть пункт меню: ").strip()
        if choice == "1":
            run_matrix_task()
        elif choice == "2":
            run_height_task()
        elif choice == "3":
            run_strikes_task()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
