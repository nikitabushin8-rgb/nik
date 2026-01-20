def main():
    # Список фильмов
    movies = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
              'Богемская рапсодия', 'Город Грехов', 'Мементо', 
              'Отступники', 'Деревня']
    favorite_movies = []

    count = int(input("Сколько фильмов хотите добавить? "))

    for _ in range(count):
        movie = input("Введите название фильма: ")
        if movie in movies:
            favorite_movies.append(movie)
        else:
            print("Ошибка: Фильма", movie, "у нас нет :(")

    if favorite_movies:
        print("Ваш список любимых фильмов:", ', '.join(favorite_movies))
    else:
        print("Вы не добавили ни одного фильма в список любимых.")

if __name__ == "__main__":
    main()