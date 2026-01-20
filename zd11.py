def make_symmetric(numbers):
    n = len(numbers)

    add_count = 0
    to_add = []

    for i in range(n):
        if numbers[i] != numbers[n - 1 - i]:
            to_add = numbers[n - 1 - i:n]  
            add_count = len(to_add)
            break
    else:
        return 0, []

    to_add.reverse()
    return add_count, to_add

def main():
    n = int(input("Количество чисел: "))
    numbers = []

    for i in range(n):
        number = int(input(f"Число: "))
        numbers.append(number)

    print(f"Последовательность: {numbers}")

    add_count, to_add = make_symmetric(numbers)

    print(f"Нужно приписать чисел: {add_count}")
    if add_count > 0:
        print(f"Сами числа: {to_add}")

if __name__ == "__main__":
    main()