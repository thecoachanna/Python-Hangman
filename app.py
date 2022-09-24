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

		
