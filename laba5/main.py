import functools
from datetime import datetime


def log_call(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print(f"[METACLASS] Викликано метод {method.__name__}()")
        return method(*args, **kwargs)
    return wrapper


class MethodDecoratorizer(type):
    def __new__(metaclass, name, bases, namespace, **kwargs):
        prefix = namespace.get("_decorated_prefix", "log_")
        for attribute, value in list(namespace.items()):
            if (
                attribute.startswith(prefix)
                and callable(value)
                and not attribute.startswith("__")
            ):
                namespace[attribute] = log_call(value)
        return super().__new__(metaclass, name, bases, namespace, **kwargs)


class Logger(metaclass=MethodDecoratorizer):
    _decorated_prefix = "log_"

    def __init__(self, name="Logger"):
        self.name = name

    def _emit(self, level, message):
        print(f"[{self.name}] {level}{message}")

    def log_message(self, message):
        self._emit("", message)

    def log_info(self, message):
        self._emit("INFO: ", message)

    def log_error(self, message):
        self._emit("ERROR: ", message)


class FileLogger(Logger):
    def __init__(self, filename="lab5_demo.log", name="FileLogger"):
        super().__init__(name)
        self.filename = filename
        self._stream = None

    def __enter__(self):
        self._stream = open(self.filename, "a", encoding="utf-8")
        print(f"Файл {self.filename} відкрито для запису логів.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._stream is not None:
            self._stream.close()
            self._stream = None
            print(f"Файл {self.filename} закрито.")
        return False

    def _emit(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} [{self.name}] {level}{message}"
        print(line)
        if self._stream is not None:
            self._stream.write(line + "\n")
            self._stream.flush()
        else:
            print("Запис у файл недоступний: контекстний менеджер не активний.")


def run_console_logging():
    print("\n--- Логування у консоль ---")
    name = input("Ім'я логера: ").strip() or "Logger"
    message = input("Повідомлення: ").strip()
    logger = Logger(name)
    logger.log_message(message)
    logger.log_info("Інформаційне повідомлення")
    logger.log_error("Тестове повідомлення про помилку")


def run_file_logging():
    print("\n--- Логування у файл через контекстний менеджер ---")
    filename = input("Назва файлу логів [lab5_demo.log]: ").strip() or "lab5_demo.log"
    message = input("Повідомлення для запису у файл: ").strip()
    try:
        with FileLogger(filename) as logger:
            logger.log_message(message)
            logger.log_info("Запис додано через FileLogger")
    except OSError as error:
        print(f"Помилка роботи з файлом: {error}")


def run_read_log():
    print("\n--- Перегляд файлу логів ---")
    filename = input("Назва файлу логів [lab5_demo.log]: ").strip() or "lab5_demo.log"
    try:
        with open(filename, "r", encoding="utf-8") as stream:
            content = stream.read()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return
    except OSError as error:
        print(f"Помилка читання файлу: {error}")
        return
    print(f"Вміст файлу {filename}:")
    print(content.rstrip() if content.strip() else "(файл порожній)")


def show_menu():
    print("\n" + "=" * 56)
    print("Лабораторна робота №5. Варіант 19")
    print("=" * 56)
    print("1. Створити Logger і записати повідомлення в консоль")
    print("2. Створити FileLogger і записати логи у файл")
    print("3. Переглянути вміст файлу логів")
    print("0. Вихід")
    print("=" * 56)


def main():
    while True:
        show_menu()
        choice = input("Оберіть пункт меню: ").strip()
        if choice == "1":
            run_console_logging()
        elif choice == "2":
            run_file_logging()
        elif choice == "3":
            run_read_log()
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
