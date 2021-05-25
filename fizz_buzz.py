class FizzBuzz():
    """FizzBuzz実行クラス"""

    def __init__(self, number):
        self.__number = number
        self.__result = ""

    # 3の倍数チェック
    def __check_fizz(self):
        """
            3の倍数の場合はself.__valueにFizzを設定
        """
        if self.__number % 3 == 0:
            self.__result = "Fizz"

    # 5の倍数チェック
    def __check_buzz(self):
        """
            5の倍数の場合はself.__valueの後ろにBuzzを設定
        """
        if self.__number % 5 == 0:
            self.__result = f"{self.__result}Buzz"

    # FizzBuzzの結果を返す
    def get_result(self):
        """
            FizzBuzzの結果を返す

            return
                result(str):FizzBuzzの結果
        """
        # 3の倍数チェック
        self.__check_fizz()

        # 5の倍数チェック
        self.__check_buzz()

        # self._valueが空文字の場合はnumberを文字列として返す
        if not self.__result:
            return str(self.__number)
        return self.__result