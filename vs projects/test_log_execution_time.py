from decorators import log_execution_time

@log_execution_time
def slow_function():
    import time
    time.sleep(2)
    return "Готово!"

if __name__ == "__main__":
    print(slow_function())
