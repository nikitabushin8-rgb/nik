def remove_highest_gpu(gpu_list):
 
    max_gpu = max(gpu_list)
    new_gpu_list = [gpu for gpu in gpu_list if gpu != max_gpu]
    return new_gpu_list

def main():
  
    count = int(input("Количество видеокарт: "))

    gpu_list = []

    for i in range(count):
        gpu = input(f"{i + 1} Видеокарта: ")
        gpu_list.append(gpu)

    print("Старый список видеокарт:", gpu_list)

    new_gpu_list = remove_highest_gpu(gpu_list)

    print("Новый список видеокарт:", new_gpu_list)

if __name__ == "__main__":
    main()