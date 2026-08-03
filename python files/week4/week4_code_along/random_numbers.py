#calling the main function
#This program create a list of numbers and append more numbers.
import random
def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)

    words = ["big","red","yellow","python","wait","calgary"]
    word_list = []
    append_random_words(words, word_list)  # ← pass words AND word_list
    print(word_list)
    append_random_words(words, word_list, 3)  # ← pass words AND word_list AND quantity
    print(word_list)

def append_random_words(words, w_list, quantity=1):  # ← added 'words' parameter
    for _ in range(quantity):
        w_list.append(random.choice(words))  # ← pick from words


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        number = random.uniform(0,100)
        number = round(number,1)
        numbers_list.append(number)


if __name__ == "__main__":
    main()