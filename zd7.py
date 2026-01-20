def calculate_parts_cost(shop):
    part_name = input("Введите название детали: ").strip().lower()

    count = 0 
    total_cost = 0 

    for item in shop:
        if item[0].lower() == part_name:
            count += 1  
            total_cost += item[1]  

    if count > 0:
        print("Количество деталей:", count)
        print("Общая стоимость:", total_cost)
    else:
        print("Детали не найдено.")

def main():
    shop = [['каретка', 1200], 
            ['шатун', 1000], 
            ['седло', 300], 
            ['педаль', 100], 
            ['седло', 1500], 
            ['рама', 12000], 
            ['обод', 2000], 
            ['шатун', 200], 
            ['седло', 2700]]

    calculate_parts_cost(shop)

if __name__ == "__main__":
    main()