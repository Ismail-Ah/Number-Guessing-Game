import random

class NumberGuess:
    difficulty_tries = [10,5,3]
    def __init__(self):
        self.show_info()
    
    def start(self):
        self.tries = 0
        self.set_difficulty()
        self.set_number()
        self.guess()

    def set_number(self):
        self.number = random.randint(0,1001)

    def show_info(self):
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n")

    def set_difficulty(self):
        print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
        self.difficulty = self.get_value("Enter your choice: ")


    def guess(self):
        user_number = self.get_value("Enter your guess: ")
        if user_number == self.number :
            print(f"Congratulations! You guessed the correct number in {self.tries} attempts.")
            return
        if user_number > self.number :
            print(f"Incorrect! The number is less than {user_number}.")
        else:
            print(f"Incorrect! The number is greater than {user_number}.")
        
        self.tries+=1
        if self.tries>self.difficulty_tries[self.difficulty-1]:
            print("Game Over")
            return
        self.guess()
        
        
        
    def get_value(self,message):
        try:
            value = int(input(message))
            return value
        except Exception as e:
            raise e

def main():
    print("test")
    game = NumberGuess()
    while(True):
        game.start()
        if(input("type exit to quit : ")=="exit"):
            break


if __name__ == "__main__":
    main()