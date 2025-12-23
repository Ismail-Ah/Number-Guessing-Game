class NumberGuess:
    def __init__(self):
        self.number = 10
    
    def guess(self):
        print(self.number)


def main():
    print("test")
    game = NumberGuess()
    game.printA()

if __name__ == "__main__":
    main()