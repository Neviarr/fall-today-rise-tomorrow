import random


def check(string):
    return string.isalpha() and string.isascii() and string.islower()


def messages(lst):
    if lst[0] == False:
        print("You should print a single letter")
        return
    if lst[1] == False:
        print("It is not an ASCII lowercase letter")
        return
    if lst[2] == False:
        print("You already typed this letter")
        return

def menu():
    action = input('Type "play" to play the game, "exit" to quit:')
    if action != "play" and action != "exit":
        menu()
    if action == "exit":
        exit()
    return

possible_words = ['python', 'java', 'kotlin', 'javascript']
answer = list(random.choice(possible_words))
word = ["-"] * len(answer)

print('H A N G M A N')
menu()

lives = 8
winner = False
already_tried = set()
while lives > 0:
    print("\n", *word, sep="")
    if "-" not in word:
        print("You guessed the word!")
        winner = True
        break

    guess = input("Input a letter: ")
    conditions = []
    conditions.append(len(guess) == 1)  # первая проверка, должен быть один символ
    conditions.append(check(guess))  # вторая проверка, буква должна быть маленькой и английской
    conditions.append(guess not in already_tried)  # третья проверка, впервые ли появляется буква


    if False not in conditions:
        already_tried.add(guess)
        if guess not in answer:
            lives -= 1
            print("No such letter in the word")
        guessed_spots = (i for i, letter in enumerate(answer) if letter == guess)
        for i in guessed_spots:
            word[i] = answer[i]
    else:
        messages(conditions)

print("You survived!" if winner else "You are hanged!")