class FizzBuzz():
    def __init__(self, number):
        self.number = number
        self.fizzFlg = 0
        self.buzzFlg = 0

    # fizzを判定するメソッド
    def fizz(self):
        if (self.number % 3 == 0):
            self.fizzFlg = 1

    # buzzを判定するクラスメソッド
    def buzz(self):
        if (self.number % 5 == 0):
            self.buzzFlg = 1
