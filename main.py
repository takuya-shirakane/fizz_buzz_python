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
    flgs.setFizzFlg()
    if (flgs.getFizzFlg()):
        item += "Fizz"

    # ５の倍数である場合はitemに"Buzz"を追加する
    flgs.setBuzzFlg()
    if (flgs.getBuzzFlg()):
        item += "Buzz"

    # itemが空文字の場合はiをlistsに追加し、それ以外はitemを追加する
    if (item == ""):
        lists.append(str(i))
    else:
        lists.append(item)

# タプルとkey-Valueに変換
fb_tp = ({i: lists[i] for i in range(0, 101)})

# 出力
for key in fb_tp:
    print(fb_tp[key])
