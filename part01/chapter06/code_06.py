# 文字列操作

# <3重クォート文字列>
""" line one
    line two
    line three
"""            #3重クォート文字列を使用して複数行の文字列を記載する

# <文字列のインデックス>
# インデックスを指定して各文字を取得
author = "Kafka"

print(author[0]) #文字列型オブジェクトauthorのインデックス「0」の値を取得
print(author[1]) #同上、インデックス「1」の値を取得
print(author[2]) #同上、インデックス「2」の値を取得
print(author[3]) #同上、インデックス「3」の値を取得
print(author[4]) #同上、インデックス「4」の値を取得

# 存在しないインデックス値を指定した場合
author = "Kafka"

try:                        #例外が発生する可能性を持つ処理であることを定義
    print(author[5])
except IndexError:          #発生する可能性のある例外を定義
    print("Invalid index!") #例外が発生した時の代わりの処理を定義

# マイナスインデックスを指定して各文字を取得
author = "Kafka"

print(author[-1]) #文字列型オブジェクトauthorのインデックス「‐1」の値を取得
print(author[-2]) #同上、インデックス「‐2」の値を取得
print(author[-3]) #同上、インデックス「‐3」の値を取得
print(author[-4]) #同上、インデックス「‐4」の値を取得
print(author[-5]) #同上、インデックス「‐5」の値を取得

# <文字列はイミュータブル(変更不可能)>
ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald" #文字列Scottを追加したい場合は新しい文字列を定義する必要がある
ff

# <文字列の足し算(連結)>
"cat" + "in" + "hat"
"cat" + " in" + " the" + " hat!" #加算演算子(+)を使用して複数の文字列を連結する

# <文字列の掛け算>
"sawyer " * 5      #積算演算子(*)を使用して文字列を繰り返す

# <大文字小文字変換>
# 全ての文字を大文字に変換
string = "We hold these truths..." #変数stringに文字列型オブジェクトを保存

result = string.upper()            #文字列型オブジェクトstringに対してupper()メソッドを使用して全ての文字を大文字に変換
print(result)

# 全ての文字を小文字に変換
string = "SO IT GOES."  #変数stringに文字列型オブジェクトを保存

result = string.lower() #文字列型オブジェクトstringに対してlowerメソッドを使用して全ての文字を小文字に変換する
print(result)

# 先頭の文字だけ大文字に変換
string = "four score and..." #変数stringに文字列型オブジェクトを保存

result = string.capitalize() #文字列型オブジェクトstringに対してcapitalizeメソッドを使用して先頭の文字だけ大文字に変換する
print(result)

# <書式化(フォーマット)>
# 書式化文字列を別の文字列に置換
"こんにちは、{}".format("ウィリアム・フォークナー") #書式化(フォーマット)文字列に対してformatメソッドを使用して別の文字列に置換する

name = "ウィリアム・フォークナー"
"こんにちは、{}".format(name)    #書式化(フォーマット)文字列に対してformatメソッドを使用して変数nameの値に置換する

# 書式化(フォーマット)文字列を何回も使用
author = "ウィリアム・フォークナー"
year_born = "1897"

"{}は、{}年に生まれました！".format(author, year_born) #2個の書式化(フォーマット)文字列に対してformatメソッドを使用して変数author・tear_bornの値に置換する

# 書式化(フォーマット)文字列とformatメソッドを使用したプログラム
what = input("何が: ")
when = input("いつ: ")
where= input("どこ: ")
do = input("どうした: ")

r = "{}は{}、{}で{}。".format(what, when, where, do) #4個の書式化(フォーマット)文字列に対してformatメソッドを使用して変数what・when・where・doの値に置換する
print(r)

# <分割>
# 文字列を分割
"水たまりを飛び越えたんだ。3メートルもあったんだぜ!".split("。") #文字列型オブジェクトに対してsplitメソッドを使用して句点で分割する

# <結合>
# 文字列の間に新しい文字列を追加
first_three = "abc"
result = "+".join(first_three) #joinメソッドを使用して文字列型オブジェクト+を文字列型オブジェクトfirst_threeの間に追加する
result

# 空文字列を追加
words = ["The", "fox", "jumped", 
        "over", "the", "fence", "."]

one = "".join(words)                 #joinメソッドを使用して文字列型オブジェクトが保存されたリスト型オブジェクトの間に空文字列を追加して結合する
one

# 空白文字列を追加
words = ["The", "fox", "jumped",
        "over", "the", "fence", "."]

one = " ".join(words)                #joinメソッドを使用して文字列型オブジェクトが保存されたリスト型オブジェクトの間に空白文字列を追加して結合する
one

# <空白除去>
# 文字列の前後の空白を取り除く
s = " The "
s = s.strip() #文字列型オブジェクトsに対してstripメソッドを使用して前後の空白を取り除く
s

# <置換>
# 指定した文字列を別の文字列に置換
equ = "All animals are equal."

equ = equ.replace("a", "@")    #文字列型オブジェクトequに対してreplaceメソッドを使用して文字列「a」を「@」に置換する
print(equ)

# <文字を探す>
"animals".index("m") #文字列型オブジェクトに対してindexメソッドを使用して文字「m」が最初に現れるインデックス値を取得

# 存在しない文字を検索した場合
try:
    "animals".index("z")
except ValueError:
    print("Not found!")

# <包含>
# 指定した文字列が含まれていることを確認
"Cat" in "Cat in the hat!"            #in演算子を使用して文字列型オブジェクトCatが含まれていることを確認
"Bat" in "Cat in the hat!"

# 指定した文字列が含まれていないこと確認
"Potter" not in "Harry"               #not in演算子を使用して文字列型オブジェクトPotterが含まれていないことを確認

# <改行>
# 指定した場所で文字列を改行
print("line1\nline2\nline3")

# <スライス>
# リストをスライス
ficts = ["トルストイ", "カミュ", "オーウェル",
         "ハクスリー", "オースティン"]

ficts[0:3]                                   #リスト型オブジェクトfictsのインデックス「0-2」のオブジェクト(要素)を取り出して新しい繰り返し可能なオブジェクト(イテラブル)を作成する

# 文字列をスライス
ivan = "死の代わりにひとつの光があった。"

print(ivan[0:6])                       #文字列型オブジェクトivanのインデックス「0-5」までのオブジェクト(要素)と取り出して新しい繰り返し可能なオブジェクト(イテラブル)を作成する
print(ivan[6:16])                      #文字列型オブジェクトivanのインデックス「6-15」までのオブジェクト(要素)を取り出して新しい繰り返し可能なオブジェクト(イテラブル)を作成する

# 開始インデックスが「0」の場合
ivan = "死の代わりにひとつの光があった。"

print(ivan[:6])                        #文字列型オブジェクトivanのインデックス「0-5」までのオブジェクト(要素)を取り出して、新しい繰り返し可能なオブジェクト(イテラブル)を作成する


# 最後のオブジェクト(要素)まで取り出す場合
ivan = "死の代わりにひとつの光があった。"

print(ivan[6:])                        #文字列型オブジェクトivanのインデックス「0-最後のオブジェクト」までのオブジェクト(要素)を取り出して、新しい繰り返し可能なオブジェクト(イテラブル)を作成する

# 開始と終了のインデックスを省略した場合
ivan = "死の代わりにひとつの光があった。"

print(ivan[:])                         #文字列型オブジェクトivanの全てのオブジェクト(要素)を取り出して、繰り返し可能なオブジェクト(イテラブル)のコピーを作成する

# <チャレンジ>
# 問題1
author = "Camus"

print(author[0])  #文字列型オブジェクトauthorのインデックス「0」の要素を取得
print(author[1])  #同上、インデックス「1」の要素を取得
print(author[2])  #同上、インデックス「2」の要素を取得
print(author[3])  #同上、インデックス「3」の要素を取得
print(author[4])  #同上、インデックス「4」の要素を取得

# 問題2
answer1 = input("What did you write yesterday?: ")
answer2 = input("Where did you sent it yesterday?: ")

new_string = "Yesterday, I wrote a {}. I sent it to {}.".format(answer1, answer2) #formatメソッドを使用して、2個の書式化(フォーマット)文字列を変数answer1・answer2の値に置き換える
print(new_string)

# 問題3
"aldous huxley was born in 1894.".capitalize() #文字列型オブジェクトに対してcapitalizeメソッドを使用して先頭の文字を大文字に変換する

# 問題4
"Where now? Who now? When now?".split("?") #文字列型オブジェクトに対してsplitメソッドを使用して「？」で分割する

# 問題5
fox = ["The", "fox", "jumped",
         "over", "the", "fence", "."]

fox = " ".join(fox)                   #joinメソッドを使用して文字列型オブジェクトが保存されたリスト型オブジェクトの要素に空白文字列を追加して結合する
fox = fox[0:-2] + "."                 #文字列型オブジェクトfoxのインデックス「0」から「-2」までのオブジェクトを取り出して新しい繰り返し可能なオブジェクト(イテラブル)を作成して、最後に文字列「.」を連結する

print(fox)

# 問題6
"A screaming comes across the sky.".replace("s", "$") #文字列型オブジェクトにreplaceメソッドを使用して文字列「s」を「$」に置換する

# 問題7
"Hemingway".index("m") #文字列型オブジェクトHemingwayに対してindexメソッドを使用して、文字列「m」が最初に現れるインデックス値を取得する

# 問題8
quote1 = "'Drink up', said Ford, 'you've got three pints to get through.'"
quote2 = '"I forgot", Lennie said softly. "I tried not to forget. Honest to God I did, George."'
quote3 = "\"Yes\", I said, \"I have a reason\", and added very softly, \"My God\"."

print(quote1)
print(quote2)
print(quote3)

# 問題9
print("three " + "three " + "three") #加算演算子(+)を使用して文字列を連結する
print("three " * 3)                  #積算演算子(*)を使用して文字列を繰り返す

# 問題10
sentence = "It was a bright cold day in April, and the clocks were striking thirteen"

inx = sentence.index(",") #文字列型オブジェクトwordsに対してindexメソッドを使用して、文字列「、」が最初に現れるインデックス値を取得する

slce = sentence[:inx]       #文字列型オブジェクトwordsのインデックス「0」から変数idxに保存されたインデックスまでスライスしてオブジェクト(要素)を取り出す
print(slce)