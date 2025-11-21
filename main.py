def hello_world(name=None):
    """Базовая функция Hello World с поддержкой персонализации"""
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

def add_numbers(a, b):
    """Новая функция для сложения двух чисел"""
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error: Both arguments must be numbers"

def personalized_greeting(name, language='en'):
    """Новая функция для персонализированных приветствий"""
    greetings = {
        'en': f'Hello, {name}!',
        'es': f'¡Hola, {name}!',
        'fr': f'Bonjour, {name}!',
        'de': f'Hallo, {name}!'
    }
    return greetings.get(language, greetings['en'])

def main():
    print(hello_world())
    print(hello_world("Alice"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(personalized_greeting("Bob", 'es'))
    print(personalized_greeting("Charlie", 'fr'))

if __name__ == "__main__":
    main()
