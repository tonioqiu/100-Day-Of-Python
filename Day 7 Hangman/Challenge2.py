from dis import dis
import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)
word_length = len(random_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
display = []
for char in random_word:
    display += "_"


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for position in range(word_length):
    letter = random_word[position]
    if letter == guess:
        display[position] = letter

print(display)