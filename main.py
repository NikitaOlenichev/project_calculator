def main():
    print("Добро пожаловать в калькулятор!")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: пожалуйста, введите числа.")


if __name__ == "__main__":
    main()