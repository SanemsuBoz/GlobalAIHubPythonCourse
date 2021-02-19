import random

name = input("What is your name? ")
print("Good Luck ! ", name)

class HangmanGame:
    
        
    def __init__(self,ch):
        self.ch=ch
                
                  
    def game(self):
          
         words = ['python', 'java', 'computer', 'engineer'] 
         print("Words List: ")
         for i in words:
             print(i,end=" ")
             
         word = random.choice(words)
         self.ch=input("Guess the characters in words list")
 
         guesses = ''
         turns = 12
         while turns > 0:
             failed = 0
             for self.ch in word: 
                 if self.ch in guesses: 
                     print(self.ch)
                 else: 
                     print("_")
                     failed += 1
             
             if failed == 0:
                 print("You Win") 
                 print("The word is: ", word) 
                 break
     
             guess = input("guess a character:")
             guesses += guess 
     
             if guess not in word:
                 turns -= 1
                 print("Wrong")
                 print("You have", + turns, 'more guesses')
                 if turns == 0:
                     print("You Loose")
                 
                 
c=HangmanGame('')
c.game()
                 
                 