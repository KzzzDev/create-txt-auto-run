import pyautogui
import random
import string


# 左上の方にカーソルを持ってきてクリック
pyautogui.click(500, 500)

# ファイルをいくつ作成するか？
# numberOfFiles = 10
numberOfFiles = 101
n = 1
alf = []

# 重複しないアルファベット2文字の組合せを100個性性
while len(alf) < numberOfFiles:
    alf = ["".join(random.sample(string.ascii_lowercase, k=2)) for _ in range(numberOfFiles)]
    alf = list(set(alf))


while n < numberOfFiles:
    # ファイルの作成処理
    # 「vi 00n.txt」を入力
    pyautogui.typewrite('vi ' + str(n).zfill(3) + '.txt')
    # returnキーを押す
    pyautogui.keyDown('return')


    # ファイル内容の入力処理
    # 入力モードに移行
    pyautogui.keyDown('i')
    pyautogui.typewrite(str(n).zfill(3) + alf[n-1] )
    # 入力モードを終了
    pyautogui.keyDown('esc')
    # 保存して閉じる
    pyautogui.typewrite(':wq')
    # returnキーを押す
    pyautogui.keyDown('return')
    n = int(n) + 1
