def main():
    n = int(input("Количество роликов: "))
    skates = []

    for i in range(n):
        size = int(input(f"Размер пары {i + 1}: "))
        skates.append(size)

    k = int(input("Количество людей: "))
    people = []

    for i in range(k):
        size = int(input(f"Размер ноги человека {i + 1}: "))
        people.append(size)

    max_people = count_people_with_skates(skates, people)

    print("Наибольшее количество людей, которые могут взять ролики:", max_people)

def count_people_with_skates(skates, people):
    skates.sort()
    people.sort()

    count = 0  
    skate_index = 0  

    for foot_size in people:
        while skate_index < len(skates):
            if skates[skate_index] == foot_size: 
                count += 1   
                skate_index += 1 
                break
            elif skates[skate_index] > foot_size: 
                break
            else:
                skate_index += 1 

    return count

if __name__ == "__main__":
    main()