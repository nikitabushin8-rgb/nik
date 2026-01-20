def josephus_problem(n, k):
    people = list(range(1, n + 1))  
    index = 0  

    while len(people) > 1:
        index = (index + k - 1) % len(people)  
        print(f"Текущий круг людей: {people}")
        print(f"Начало счёта с номера {people[index]}")
        print(f"Выбывает человек под номером {people[index]}")
        people.pop(index) 
    return people[0]  

def main():

    n = int(input("Количество человек: "))
    k = int(input("Какое число в считалке? "))

    last_person = josephus_problem(n, k) 
    print(f"Остался человек под номером {last_person}")

if __name__ == "__main__":
    main()