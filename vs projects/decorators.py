import time
import json
from functools import wraps
# Завдання 1: Декоратор для логування часу виконання функції
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {execution_time:.4f} секунд")
        return result
    return wrapper
# Завдання 2: Декоратор для валідації аргументів функції
def validate_arguments(types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {arg} не відповідає очікуваному типу {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# Завдання 3: Декоратор для кешування результатів функції в файл
def cache_to_file(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                with open(filename, 'r') as file:
                    cache = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                cache = {}

            cache_key = f"{func.__name__}_{args}_{kwargs}"
            if cache_key in cache:
                print(f"Результат для {cache_key} взятий з кешу.")
                return cache[cache_key]

            result = func(*args, **kwargs)
            cache[cache_key] = result

            with open(filename, 'w') as file:
                json.dump(cache, file, ensure_ascii=False, indent=4)

            return result
        return wrapper
    return decorator
