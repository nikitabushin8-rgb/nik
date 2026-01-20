def calculate_total_time(songs, selected_songs):
    total_time = 0 
    for song in selected_songs:
        for track in songs:
            if track[0] == song:  
                total_time += track[1] 
                break  
    return total_time

def main():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]

    n = int(input("Сколько песен выбрать? "))
    selected_songs = []

    for i in range(n):
        song_name = input(f"Название {i + 1}-й песни: ")
        selected_songs.append(song_name)

    total_time = calculate_total_time(violator_songs, selected_songs)

    print(f"Общее время звучания песен — {total_time:.2f} минуты")

if __name__ == "__main__":
    main()