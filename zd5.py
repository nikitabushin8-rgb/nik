def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

def main():
    n = int(input("Введите количество чисел в списке: "))

    numbers = []
    for i in range(n):
        number = int(input(f"Введите число {i + 1}: "))
        numbers.append(number)

    print("Изначальный список:", numbers)

    bubble_sort(numbers)

    print("Отсортированный список:", numbers)

if __name__ == "__main__":
    main()