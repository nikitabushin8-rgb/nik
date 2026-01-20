def cyclic_right_shift(original_list, shift):
    n = len(original_list)
    if n == 0:
        return original_list  

    shift = shift % n

    return original_list[-shift:] + original_list[:-shift]

def main():
    n = int(input("Введите количество элементов в списке: "))
    original_list = []

    for i in range(n):
        element = int(input(f"Элемент {i + 1}: "))
        original_list.append(element)

    shift = int(input("Сдвиг: "))

    print("Изначальный список:", original_list)

    shifted_list = cyclic_right_shift(original_list, shift)
    print("Сдвинутый список:", shifted_list)

if __name__ == "__main__":
    main()