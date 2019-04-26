'''
Quick hackey code to create a basic hangman game in the terminal.

@author Ed
@date April 2019
'''

'''
Print the dude.
PRECON: step is an int between 0 and 6.
'''
def printman(step):
    if step == 0:
      result = "              ------\n\
              |    |\n\
              |    \n\
              |   \n\
              |    \n\
              |   \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 1:
        result = "              ------\n\
              |    |\n\
              |    @\n\
              |   \n\
              |   \n\
              |   \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 2:
      result = "              ------\n\
              |    |\n\
              |    @\n\
              |    |  \n\
              |    | \n\
              |    \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 3:
        result = "              ------\n\
              |    |\n\
              |    @\n\
              |   /| \n\
              |    | \n\
              |    \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 4:
      result = "              ------\n\
              |    |\n\
              |    @\n\
              |   /|\\ \n\
              |    | \n\
              |   \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 5:
        result = "              ------\n\
              |    |\n\
              |    @\n\
              |   /|\\ \n\
              |    | \n\
              |   / \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    elif step == 6:
      result = "              ------\n\
              |    |\n\
              |    @\n\
              |   /|\\ \n\
              |    | \n\
              |   / \\ \n\
          ____|__________\n\
         /    |         /| \n\
        /______________/ / \n\
        |______________|/"
    print(result)


'''
The actual game. Start with player 1 entering a word, this is then hidden by printing
a load of new lines.

Player 2 must then guess the word by entering only 1 character.
'''
def game():
    print("PLAYER 1- Please enter your word:")
    word = input()
    length = len(word)
    blank = "_"*length
    print("\n"*100)
    guesses = []
    game_is_running = True
    step = 0
    while(game_is_running):
        print(blank)
        print("Previous guesses: " +str(guesses))
        print("PLAYER 2- Guess a letter:")
        guess = input()
        if len(guess)==1:
        	if guess in guesses:
        		print("Already guessed that letter.")
        	else:
	            if guess in word:
	                for i in range(len(word)):
	                    if word[i] == guess:
	                        blank = blank[:i]+word[i]+blank[i+1:]
	                if blank == word:
	                    game_is_running = False
	                    print("Player 2 wins! The word was: {}".format(word))
	            else:
	                printman(step)
	                step += 1
	                if step==7:
	                    game_is_running = False
	                    print("Player 1 wins! The word was: {}".format(word))
	                guesses.append(guess)
        else:
            print("Please type only 1 character.")


'''
Here is where the loop for the game takes place. Once any player wins, the game will
ask if you would like to play again.
'''
def main():
    flag_1 = True
    flag_2 = True
    while(flag_1):
        game()
        print("Play again?")
        flag_2 = True
        while(flag_2):
            x = input()
            if x == "n":
                flag_1 = False
                flag_2 = False
            elif x == "y":
                print("Starting again!")
                flag_2 = False
            else:
                print("Please type y or n.")


if __name__ == "__main__":
    main()