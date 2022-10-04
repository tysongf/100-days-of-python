class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.right = 0
        self.wrong = 0

    def add_right(self):
        print("\nCorrect!\n")
        self.right += 1

    def add_wrong(self):
        print("\nWrong!\n")
        self.wrong += 1

    def reset_score(self):
        self.__init__(self.name)
