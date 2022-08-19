from random import randint


def main():
    gen = generate_num()
    is_num(gen)


def generate_num():
    generate = randint(0, 10)
    print(f'Я загадал {generate}')
    return int(generate)


def is_num(generate):
    while True:
        check_num = int(input("Введите число: "))
        if check_num == generate:
            print("Вы угадали число!")
            break
        elif check_num >= generate:
            print("Вы указали число больше, чем я загадал")
        elif 0 <= check_num <= generate:
            print("Вы указали число меньше, чем я закадал")
        else:
            print("Вы ввели некорректное число")


if __name__ == '__main__':
    main()
