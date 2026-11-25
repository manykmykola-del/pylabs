import itertools
import time
from functools import wraps


def retry(attempts=3, delay=0.5):
    if attempts < 1:
        raise ValueError("Кількість спроб має бути не меншою за 1.")
    if delay < 0:
        raise ValueError("Затримка не може бути від'ємною.")

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, attempts + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"Спроба {attempt}/{attempts} не вдалася: {error}")
                    if attempt < attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator


class FlakyService:
    def __init__(self, failures_before_success=2):
        self.failures_before_success = failures_before_success
        self.calls = 0

    @retry(attempts=4, delay=0.2)
    def fetch_data(self):
        self.calls += 1
        if self.calls <= self.failures_before_success:
            raise ConnectionError("Сервіс тимчасово недоступний")
        return {"data": f"value-{self.calls}"}


def run_retry_task():
    print("\n--- Завдання 1: декоратор @retry ---")
    service = FlakyService(failures_before_success=2)
    try:
        result = service.fetch_data()
        print(f"Успішний результат: {result}")
    except ConnectionError as error:
        print(f"Не вдалося отримати дані: {error}")

    print("\nПеревірка вичерпання всіх спроб:")
    failing_service = FlakyService(failures_before_success=10)
    try:
        failing_service.fetch_data()
    except ConnectionError as error:
        print(f"Після всіх спроб виняток прокинуто далі: {error}")


def card_value(rank):
    named_values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    upper_rank = rank.upper()
    if upper_rank in named_values:
        return named_values[upper_rank]
    return int(rank)


def is_even_card_value(pair):
    rank, suit = pair
    return card_value(rank) % 2 == 0


def generate_valid_card_pairs(ranks, suits):
    all_pairs = itertools.product(ranks, suits)
    return list(filter(is_even_card_value, all_pairs))


def run_cartesian_task():
    print("\n--- Завдання 2: декартовий добуток з фільтрацією ---")
    ranks = ["10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    pairs = generate_valid_card_pairs(ranks, suits)
    print(f"Усього можливих пар (карта, масть): {len(ranks) * len(suits)}")
    print(f"Після фільтрації (парне числове значення карти): {len(pairs)}")
    for rank, suit in pairs:
        print(f"  ({rank}, {suit})")


def show_menu():
    print("\n" + "=" * 52)
    print("Лабораторна робота №4. Варіант 6 / Варіант 8")
    print("=" * 52)
    print("1. Декоратор @retry (завдання 1, варіант 6)")
    print("2. Декартовий добуток з фільтрацією (завдання 2, варіант 8)")
    print("0. Вихід")
    print("=" * 52)


def main():
    while True:
        show_menu()
        choice = input("Оберіть пункт меню: ").strip()
        if choice == "1":
            run_retry_task()
        elif choice == "2":
            run_cartesian_task()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
