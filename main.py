def hello_world():
    """Базовая функция Hello World"""
    return "Hello, World!"

def add_numbers(a, b):
    """Новая функция для сложения двух чисел"""
    return a + b

def main():
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")

if __name__ == "__main__":
    main()
