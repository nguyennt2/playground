import random

lives = 3
word_list = ["ardvark", "baloon", "camel"]
chosen_word = random.choice(word_list);

display = []
for letter in chosen_word:
    display += "_"

end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter:").lower()
    char_found = False
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = user_guess
            char_found = True
    if char_found == False:
        print(f"Letter {user_guess} is not matched.")
        lives -= 1

    if "_" not in display:
        print('You win.')
        end_of_game = True
        print(f"Final word: {chosen_word}")
    elif lives <= 0:
        print("You lose.")
        end_of_game = True
    else:
        print(display)
