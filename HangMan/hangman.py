import random

player_name = input("Enter your name\n")


def man(num):
    if num == 1:
        return "----------\n" \
               "     0     "
    elif num == 2:
        return "----------\n" \
               "     0    \n" \
               "     |      "
    elif num == 3:
        return "----------\n" \
               "     0    \n" \
               "    /|    \n"
    elif num == 4:
        return "----------\n" \
               "     0    \n" \
               "    /|\     "
    elif num == 5:
        return "----------\n" \
               "     0    \n" \
               "    /|\   \n" \
               "     |      "
    elif num == 6:
        return "----------\n" \
               "     0    \n" \
               "    /|\   \n" \
               "     |    \n" \
               "    /      "
    else:
        return "----------\n" \
               "     0    \n" \
               "    /|\   \n" \
               "     |    \n" \
               "    / \     "


while True:
    word_list = []
    with open("wordList.txt", "r+") as words:
        for word in words:
            word = str(word).rstrip("\n")
            if len(word) > 2:
                word_list.append(word)

    random_number = random.randint(1, 9477)
    word_to_guess = "hello"  # word_list[random_number]
    word_after_guess = []
    wrong_guess = 0
    for _ in range(0, len(word_to_guess)):
        word_after_guess.append("_")
    print("".join(word_after_guess))
    while True:
        word_guessed = input("Take a guess ")
        if word_guessed in word_to_guess:
            loc = word_to_guess.index(word_guessed)
            word_after_guess[loc] = word_guessed
            print("".join(word_after_guess))
            if "_" not in word_after_guess:
                print(f'Congratulation {player_name} You Win!!, You Guessed right')
                break
        else:
            print("".join(word_after_guess))
            wrong_guess += 1
            print(man(wrong_guess))
            if wrong_guess == 7:
                print("Game Over")
                break

    y_n = input("Do you wanna play again(y/n):")
    if y_n == 'N' or y_n == 'n':
        break
