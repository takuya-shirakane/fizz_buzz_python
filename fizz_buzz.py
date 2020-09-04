class FizzBuzz():
    def __init__(self, number):
        self._number = number
        self._fizzFlg = 0
        self._buzzFlg = 0

    # fizzを判定するメソッド
    def setFizzFlg(self):
        if (self._number % 3 == 0):
            self._fizzFlg = 1

    # buzzを判定するクラスメソッド
    def setBuzzFlg(self):
        if (self._number % 5 == 0):
            self._buzzFlg = 1

    # fizzFlgを取得するメソッド
    def getFizzFlg(self):
        return self._fizzFlg

    # buzzFlgを取得するメソッド
    def getBuzzFlg(self):
        return self._buzzFlg
