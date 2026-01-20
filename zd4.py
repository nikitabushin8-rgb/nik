def is_palindrome(word):
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]

def main():
    word = input("Введите слово: ")

    if is_palindrome(word):
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

if __name__ == "__main__":
    main()
