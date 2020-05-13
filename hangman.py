from random import seed, randint
print("H A N G M A N")
while True:
    print('Type "play" to play the game, "exit" to quit:')
    prompt = input()
    if prompt == "play":
        pass
    elif prompt == "exit":
        break
    else:
        continue
    word_list = ['python', 'java', 'kotlin', 'javascript']
    w_number = randint(0, 3)
    word_hint = word_list[w_number]
    output = "-" * len(word_hint)
    temp_output_list = list(output)
    letter_set = set(word_hint)
    won = False
    health = 8
    entered_values = list()
    while health > 0:
        print()
        print(output)
        guess = input("Input a letter: ")
        count = 0
        if len(guess) >= 2 or len(guess) <= 0:
            print("You should print a single letter")
            continue
        if guess != guess.lower() or not guess.isalpha():
            print('It is not an ASCII lowercase letter.')
            continue
        if guess not in entered_values:
            entered_values.append(guess)
        elif guess in entered_values:
            print("You already typed this letter")
            continue
        if guess not in word_hint:
            print("No such letter in the word")
            health -= 1
            continue
        for letter in word_hint:
            if guess == letter:
                temp_output_list[count] = word_hint[count]
            count += 1
        output = ''.join(temp_output_list)
        if output == word_hint:
            won = True
            print(output)
            print("You guessed the word!")
            break
    if won is True:
        print("You survived!")
    else:
        print("You are hanged!")
