from decorators import validate_arguments

@validate_arguments((int, str))
def process_data(number, text):
    return f"Число: {number}, Текст: {text}"

if __name__ == "__main__":
    try:
        print(process_data(42, "Hello"))  
        print(process_data(42, 100))     
    except TypeError as e:
        print(e)
