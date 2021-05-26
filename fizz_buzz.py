class FizzBuzz():
    """FizzBuzz実行クラス"""

    def __init__(self, number):
        self.__number = number
        self.__result = ""

    def set_result(self, value):
        """
            __resultに値をセットする
        """
        self.__result = f"{self.__result}{value}"

    def get_result(self):
        """
            FizzBuzzの結果を返す

            return
                result(str):FizzBuzzの結果
        """
        # self.__resultが空文字の場合はself.__numberを文字列として返す
        if not self.__result:
            return str(self.__number)
        return self.__result