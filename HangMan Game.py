import random
stages= [ """
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
"""]

end_of_game = False
word_list = ["starwars","python","elephant","lion","optimusprime","megatron","darthvader"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


display = []
for _ in range(word_length):
    display += "_"

print(display)

while not end_of_game:  
    guess = input("Guess a letter: \n").lower()



    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessedletter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print("That letter is not in the word!")
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")


