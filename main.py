from fizz_buzz import FizzBuzz

lists = []

for i in range(0, 101):
    # iが０の場合
    if (i == 0):
        lists.append(str(i))
        continue

    flgs = FizzBuzz(i)
    item = ""

    # ３の倍数である場合はitemに"Fizz"を追加する
    flgs.fizz()
    if (flgs.fizzFlg):
        item += "Fizz"

    # ５の倍数である場合はitemに"Buzz"を追加する
    flgs.buzz()
    if (flgs.buzzFlg):
        item += "Buzz"

    # itemが空文字の場合はiをlistsに追加し、それ以外はitemを追加する
    if (item == ""):
        lists.append(str(i))
    else:
        lists.append(item)

    # リストの中身を表示する
    print(lists[i])

print(lists)
