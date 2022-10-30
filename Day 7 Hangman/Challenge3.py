from dis import dis
import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
word_length = len(random_word)
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    display = []
    for char in random_word:
        display += "_"


    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Win")
