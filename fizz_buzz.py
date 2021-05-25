class FizzBuzz():
    def __init__(self, number):
        self._number = number
        self._value = ""

    # 3の倍数チェック
    def check_fizz(self):
        if self._number % 3 == 0:
            self._value = "Fizz"

    # 5の倍数チェック
    def check_buzz(self):
        if self._number % 5 == 0:
            self._value = f"{self._value}Buzz"

    # 格納する値を返す
    def get_value(self):
        if not self._value:
            # self._valueが空文字の場合はnumberを文字列として返す
            return str(self._number)
        return self._value