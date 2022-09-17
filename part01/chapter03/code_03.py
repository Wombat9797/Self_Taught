# プログラミング入門

# 「Hello, World!」を100回出力する
for i in range(100):
    print("Hello, World!")

# <これはコメントです>
print("Hello, World!")

# <出力>
print("Python")
print("こんにちは")
print("""これは、とても、とても、
        とても、とても長い複数行の
        コードです。""")

# <行>
"line1"
"line2"
"line3"

# バックスラッシュ(\ or ¥)
print\
("""これは、とても、とても、とても、
    とても長い複数行のコードです。""")

# <スペース>
for i in range(100):
    print("Hello, World!") #インデントでコードブロックの開始と終了を示す

# <データ型>
# 文字列(str)データ型
print("Hello, World!")
print('Hello, World!')

# 整数(int)データ型
1
5
100

# 浮動小数点数(float)データ型
2.2 + 2.2
5.5 * 1.5

# ブール(bool)データ型
True
False

# NoneTypeデータ型
None

# 定数
print(2 + 2)
print(2 - 2)
print(4 / 2)
print(2 * 2)

# <変数>
# 変数の定義
b = 100 #変数bに整数型オブジェクト100を保存
b

# 変数の値を変更
x = 100
print(x)

x = 200  #変数x整数型オブジェクト200を再保存
print(x)

# 変数を使用した計算
x = 10
y = 10    #変数x.yに整数型オブジェクト10を保存
z = x + y #変数zに計算結果を保存
print(z)

a = x - y #変数aに計算結果を保存
print(a)

# インクリメント(増加)
x = 10
x = x + 1 #変数xに「+1」した値を再保存
print(x)

# インクリメント(省略)
x = 10
x += 1   #変数xに「+1」した値を再保存
print(x)

# ディクリメント(減少)
x = 10
x = x - 1 #変数xに「-1」した値を再保存
print(x)

# ディクリメント(省略形)
x = 10
x -= 1   #変数xに「-1」した値を再保存
print(x)

# 文字列(str)型オブジェクトを保存
hi = "Hello, World!"
print(hi)

# 浮動小数点数(float)型オブジェクトを保存
my_float = 2.2
print(my_float)

# ブール(bool)型オブジェクトを保存
my_boolean = True
print(my_boolean)

# <構文>
# Pythonの構文の例(文字列)
print("Hello, World!")

# <エラーと例外>
# 例外の例1(ZeroDivisionError)
10 / 0

# 例外の例2(IndentationError)
y = 2
        #x = 1

# <算術演算子>
# 加算(+)演算子
print(2 + 2)

# 減算(-)演算子
print(7 - 1)

# 積算(*)演算子
print(8 * 2)

# 除算(/)演算子1
print(13 / 8)
print(14 / 3)

# 除算(//)演算子2
print(13 // 8)
print(13 // 5)
print(14 // 3)

# 剰余(%)演算子
print(14 % 4)
print(13 % 5)

# 累乗(**)演算子
print(2 ** 3)
print(10 ** 3)

# 偶数
print(12 % 2)

# 奇数
print(11 % 2)

# 演算子の優先順位
print(2 + 2 * 2)   #掛け算は足し算より優先順位が高い
print((2 + 2) * 2) #括弧は掛け算より優先順位が高い

# <比較演算子>
# より大きい(>)
100 > 10

# より小さい(<)
100 < 10

# 以上(>=)
2 >= 2

# 以下(<=)
1 <= 4
2 <= 2

# 等価(==)
6 == 9
2 == 2
1 == 2

# 非等価(!=)
3 != 2
1 != 2
2 != 2

# <論理演算子>
# かつ(and)
1 == 1 and 2 == 2
1 == 2 and 2 == 2
1 == 2 and 2 == 1
2 == 1 and 1 == 1
1 == 1 and 10 != 2 and 2 < 10 #論理演算子andを複数回使用する

# あるいは(or)
1 == 1 or 1 == 2
1 == 1 or 2 == 2
1 == 2 or 2 == 1
2 == 1 or 1 == 2
1 == 1 or 1 == 2 or 1 == 3 #論理演算子orを複数回使用する

# 否定(not)
not 1 == 1
not 1 == 2

# <条件式>
# if-else文の定義
home = "America"
if home == "America":        #条件式を定義する
    print("Hello, America!") #条件式がTrueなので、こちらのコードブロックが実行される
else:
    print("Hello, World!")   

home = "Japan"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")   #条件式がFlaseなので、こちらのコードブロックが実行される

# else文を省略
home = "America"
if home == "America":
    print("Hello, America!") #条件式がTrueなので、こちらのコードブロックを実行する

home = "Japan"
if home == "America":
    print("Hello, America!") #条件式がFlaseの場合のコードブロックが定義されていないので、何も出力されない

# 複数のif文
# 評価判定がTrueのコードブロックのみ実行される
x = 2
if x == 2:
    print("数値は2です。")
if x % 2 == 0:
    print("数値は偶数です。")
if x % 2 != 0:
    print("数値は奇数です。")

# if文をネスト(入れ子)
x = 10
y = 11

if x == 10:
    if y == 11:      #ネストされた条件文を定義
        print(x + y) #両方の条件式がTrueの場合に実行されるコードブロック

# if-elif-else文の定義
home = "Thailand"
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

# if-elif-else文(全ての条件式がFalse評価の場合)
home = "Mars"
if home == "America":
    print("Hello, America!")
elif home == "Canada":
    print("Hello, Canada!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "Mexio":
    print("Hello, Mexio")
else:
    print("Hello, World!")

# if文やelif文を何度も書いた例
x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don't Know!")

if x == 100:               #条件式がFalseの場合は何も出力しない(条件式がFalseの場合のコードブロックが定義されていない)
    print("x is 100!")

if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")

# <文>
# 単純文の例
print("Hello, World!")
2 + 2

# 複合文の例
for i in range(100):       #ヘッダー部分
    print("Hello, World!") #スイート部分

# 複数の節を持つ複合文
x = 100

if x == 10:                #ヘッダー部分1 / 一つ目の節
    print("10!")           #スイート部分1
elif x == 20:              #ヘッダー部分2 / 二つ目の節
    print("20!")           #スイート部分2
else:                      #ヘッダー部分3 / 三つ目の節
    print("I don't knoe!") #スイート部分3

if x == 100:               #ヘッダー部分1
    print("x is 100!")     #スイート部分2

if x % 2 == 0:             #ヘッダー部分1 / 一つ目の節
    print("x is even!")    #スイート部分1
else:                      #ヘッダー部分2 / 二つ目の節
    print("x is odd!")     #スイート部分2

# 空文(空の行)
print("Michael")
                 #空の文(空の行)はプログラムを実行しても反映されない

print("Jordan")

# <チャレンジ>
# 問題1
print("Good morning!")
print("Good afternoon!")
print("Good evening!")

# 問題2
x = 10                      #変数xに整数型オブジェクトを保存
if x < 10:
    print("x is less than 10!")
else:
    print("x is greater than or equal to 10!")

# 問題3
x = 26                                #変数xに整数型オブジェクトを保存
if x <= 10:
    print("x is less than or equal to 10!")
elif x <= 25:
    print("x is greater than 10, but less than or equal to 25!")
else:
    print("x is greater than 25!")

# 問題4
print(100 % 13)

# 問題5
print(100 // 6)

# 問題6
age = 36
retirement = 65 - age

if retirement < 10:
    print("You get to retire soon!")
else:
    print("Wow, you have a long time until you can get retire!")