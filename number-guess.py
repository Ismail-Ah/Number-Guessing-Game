import random
import time
import os
from pathlib import Path

FILE = Path("score.txt")

class NumberGuess:
    difficulty_tries = [10,5,3]
    def __init__(self):
        self.show_info()
    
    def start(self):
        self.start_time = time.time()
        self.tries = 0
        self.set_difficulty()
        self.set_number()
        self.guess()

    def set_number(self):
        self.number = random.randint(0,10)

    def show_info(self):
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n")

    def set_difficulty(self):
        print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
        self.difficulty = self.get_value("Enter your choice: ")
        while(self.difficulty<1 or self.difficulty>3):
            print("You should enter a number between 1 and 3")
            self.difficulty = self.get_value("Enter your choice: ")
        print()


    def guess(self):
        user_number = self.get_value("Enter your guess: ")
        if user_number == self.number :
            guessing_time = time.time()-self.start_time
            print(f"Congratulations! You guessed the correct number in {self.tries+1} attempts.")
            print(f"Your time is : {guessing_time:.2f} seconds\n")
            self.set_score(self.difficulty,self.tries+1)
            best_score = self.get_best_score(self.difficulty)
            print(f"Best Score : {best_score}")
            return
        if user_number > self.number :
            print(f"Incorrect! The number is less than {user_number}.")
        else:
            print(f"Incorrect! The number is greater than {user_number}.")
        
        self.tries+=1
        if self.tries>self.difficulty_tries[self.difficulty-1]:
            print("Game Over")
            return
        print()
        self.guess()

    def get_best_score(self,difficulty):
        if not FILE.exists():
            FILE.touch()
            with open(FILE,"w") as file:
                file.write("-1,-1,-1")
        with open(FILE,"r") as file:
            scores = [int(s) for s in file.read().split(",")]
            return scores[difficulty-1]
        
    def set_score(self,difficulty,score):
        if not FILE.exists():
            FILE.touch()
            with open(FILE,"w") as file:
                file.write("-1,-1,-1")
        with open(FILE,"r") as file:
            scores = [int(s) for s in file.read().split(",")]
        if(scores[difficulty-1]>score or scores[difficulty-1]==-1):
            scores[difficulty-1] = score
        with open(FILE,"w") as file:
            file.write(f"{scores[0]},{scores[1]},{scores[2]}")
        

        
        
        
    def get_value(self,message):
        while(True):
            value = input(message)
            try:
                return int(value)
            except:
                print("please enter an int")

def main():
    print(time.time())
    print("test")
    game = NumberGuess()
    while(True):
        game.start()
        if(input("type exit to quit : ")=="exit"):
            break
        print()


if __name__ == "__main__":
    main()