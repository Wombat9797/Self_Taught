# モジュール

# <別のモジュールをインポート>
# 自作モジュールをインポート
def print_hello():
    print("Hello, world!")

# 指定したプログラム以外は実行しない
if __name__ == "__main__":
    print("Hello")

# <チャレンジ>
# 問題2
import math

def cube_it(x, y=3):
    return math.pow(x, y) #mathモジュールのpow関数を使用して引数xのy乗を計算