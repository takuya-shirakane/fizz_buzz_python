from fizz_buzz import FizzBuzz

# 定数
MIN = 1
MAX = 100

def main():
    values = []

    # 出力値設定ループ
    for i in range(MIN, MAX + 1):
        # インスタンス生成
        fizzBuzz = FizzBuzz(i)

        # 3の倍数チェック
        fizzBuzz.check_fizz()

        # 5の倍数チェック
        fizzBuzz.check_buzz()

        # リストに格納
        values.append(fizzBuzz.get_value())

    # コンソールに出力
    print("\n".join(values))

if __name__ == "__main__":
    main()