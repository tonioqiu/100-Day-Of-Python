print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine both names and convert to lower case
combined_names = name1 + name2
combined_names = combined_names.lower()

# Count the number of times the letters "t", "r", "u", "e" appear in the combined string
true = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")

#count the number of times the letters "l", "o", "v", "e" appear in the combined string
love = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

# Convert the true and love counts to a two digit number
score = int(str(true) + str(love))

# Use if/elif/else to determine the message based on the score
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
