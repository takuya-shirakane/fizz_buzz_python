from fizz_buzz import FizzBuzz
from constant import Constant as const


def main():
    values = []

    start = const.MIN
    finish = const.MAX + 1

    # 出力値設定ループ
    for i in range(start, finish):
        # インスタンス生成
        fizzBuzz = FizzBuzz(i)

        # 3の倍数チェック
        if i % 3 == 0:
            fizzBuzz.set_result("Fizz")

        # 5の倍数チェック
        if i % 5 == 0:
            fizzBuzz.set_result("Buzz")

        # リストに格納
        values.append(fizzBuzz.get_result())

    # コンソールに出力
    print("\n".join(values))

if __name__ == "__main__":
    main()