from decorators import cache_to_file

@cache_to_file("cache.json")
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 5))
    print(add(3, 5))  
