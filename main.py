from fizz_buzz import FizzBuzz

# 定数
MIN = 1
MAX = 100

def main():
    lists = []

    for i in range(MIN, MAX + 1):
        fizzBuzz = FizzBuzz(i)

        # 3の倍数チェック
        fizzBuzz.check_fizz()

        # 5の倍数チェック
        fizzBuzz.check_buzz()

        # リストに格納
        lists.append(fizzBuzz.get_value())

    # コンソールに出力
    print("\n".join(lists))

if __name__ == "__main__":
    main()