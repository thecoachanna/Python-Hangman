import random
from hangman_words import word_list

class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.word_length = (len(self.chosen_word))
        self.guess = ['_']*self.word_length
        self.lives = 6

    def __str__(self):
        return self.chosen_word

    def show(self):
        for ch in self.guess:
            print(ch, end='')
        print()

    def check(self, ch):
        if ch in self.chosen_word:
            for i in range(self.word_length):
                if self.chosen_word[i] == ch:
                    self.guess[i] = ch
            return True
        else:
            return False

    def play_game(self):
        picked_ch = ''
        while self.lives > 0: 
 
            self.show()
            print("You have ", self.lives, "lives.")
            print(picked_ch)
            ch = input("Please guess a letter: ")
            picked_ch += ch + ', '
            if self.check(ch):
                print("Correct!")
                if '-' not in self.guess:
                    break               
            else:
                print("Wrong!")
                self.lives -= 1

        if self.lives == 0:
            print("Game over, you lose.")
        else:
            print("You won!")


chosen_word = random.choice(word_list)
game = Word(chosen_word)    
game.play_game()

		

# def stage():
# 	os.system("clear")
# 	print(hangman_art.stages[8-lives])
# 	print(' '.join([str(l) for l in display]))
# 	print(f"You have {lives} lives.")

# print(stages[self.lives])




















# from hangman_art import stages, logo
# from hangman_words import word_list

# # Choose a random word.
# chosen_word = random.choice(word_list)
# word_length = (len(chosen_word))
# end_of_game = False
# lives = 6

# print(logo)

# # Create blanks.
# display = []
# for _ in range(word_length):
#     display += '_'

# while not end_of_game:
# # Guess a letter.
#     guess = input('Guess a letter: ').lower()
#     if guess in display:
#         print(f"You've already guessed {guess}.")

#     # Check if guessed letter matches chosen_word.
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
            
#   #Check if user is wrong.          
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print('You lose.')      

#     #Join all the elements in the list and turns it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print('You win!')

#     print(stages[lives])