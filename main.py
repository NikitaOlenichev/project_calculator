def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Добро пожаловать в калькулятор!")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Выберите функцию:\n1. Сложение;\n2. Вычитание.")
        value = int(input("Введите номер функции: "))
        match value:
            case 1:
                print(f"Результат: {a} + {b} = {add(a, b)}")
            case 2:
                print(f"Результат: {a} - {b} = {subtract(a, b)}")
            case _:
                print("Неизвестная функция!!!!")
    except ValueError:
        print("Ошибка: пожалуйста, введите числа.")


if __name__ == "__main__":
    main()