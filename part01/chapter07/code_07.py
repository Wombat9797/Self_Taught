# ループ

# <forループ>
# 文字列の要素を繰り返す例
import numbers


name = "Ted"

for character in name: #変数characterにイテラブルなオブジェクトnameの要素を1つずつ割り当てる
    print(character)

# リストの要素を繰り返す例
shows = ["GOT", "Narocs", "Vice"] #変数showsにリスト型オブジェクト(イテラブル)を保存

for show in shows:                #変数showにイテラブルなオブジェクトshowsに要素を1つずつ割り当てる
    print(show)

# タプルの要素を繰り返す例
coms = ("A. Development", "Friends", "Always Sunny") #変数comsにタプル型オブジェクト(イテラブル)を保存

for show in coms:                                    #変数showにイテラブルなオブジェクトcomsの要素を1つずつ割り当てる
    print(show)

# 辞書のキーを繰り返す例
people = {"G. Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"}        #変数peopleに辞書型オブジェクト(イテラブル)を保存

for character in people:                   #変数characterにイテラブルなオブジェクトpeopleのキーを1つずつ割り当てる
    print(character)

# リストをオブジェクト(要素)を更新
tv = ["Got", "Narcos", "Vice"]
i = 0                          #インデックス変数iに整数型オブジェクト0を保存

for show in tv:                #変数showにイテラブルなオブジェクトtvの要素を1つずつ割り当てる
    new = tv[i]                #変数newにインデックス変数iに該当するオブジェクト(要素)を保存
    new = new.upper()          #文字列型オブジェクトnewに対してupperメソッドを使用して変数newに再保存
    tv[i] = new                #インデックス変数iに該当するオブジェクト(要素)に変数newの値を再保存
    i += 1                     #インデックス変数iをインクリメントして再保存

print(tv)                      #ループ処理が完了したらリスト型オブジェクトtvを出力
                               #ループ処理の回数はイテラブルなオブジェクトtvの要素数と同じになる

# enumerate()関数を使用してリストを更新
tv = ["got", "narcos", "vice"]

for i, new in enumerate(tv):   #enumerate関数を使用してイテラブルなオブジェクトtvのインデックスをインデックス変数iに、オブジェクト(要素)を変数newに1つずつ割り当てる
    new = tv[i]                #変数newにインデックス変数iに該当する要素を保存
    new = new.upper()          #文字列型オブジェクトnewに対してupperメソッドを使用して変数newに再保存
    tv[i] = new                #インデックス変数iに該当する要素に変数newの値を再保存

print(tv)                      #ループ処理が完了したらリスト型オブジェクトを出力
                               #ループ回数はイテラブルなオブジェクトtvの要素数と同じになる

# リストのデータを加工して新しいリストを作成
tv = ["got", "narcos", "vice"]
coms = ["arrested development", "friends", "always sunny"]
all_shows = []                                             #変数all_showsに空のリスト型オブジェクトを保存

for show in tv:                                            #変数showにイテラブルなオブジェクトtvの要素を1つずつ割り当てる
    show = show.upper()                                    #文字列型オブジェクトshowに対してupperメソッドを使用して変数showに再保存
    all_shows.append(show)                                 #リスト型オブジェクトall_showsに対してappendメソッドを使用して変数showの値を追加する
                                                           #ループ処理の回数はイテラブルなオブジェクトtvの要素数(3)と同じになる

for show in coms:                                          #変数showにイテラブルなオブジェクトcomsの要素を1つずつ割り当てる
    show = show.upper()                                    #文字列型オブジェクトshowに対してupperメソッドを使用して変数showに再保存
    all_shows.append(show)                                 #リスト型オブジェクトall_showsに対してappendメソッドを使用して変数showの値を追加する
                                                           #ループ処理の回数はイテラブルなオブジェクトcomsの要素数(3)と同じになる

print(all_shows)                                           #ループ処理が完了したらリスト型オブジェクトall_showsを出力

# range関数
for i in range(1, 11): #変数iにrange関数の整数列(イテラブル)の要素を1つずつ割り当てる
    print(i)

# <whileループ>
# whileループの定義
x = 10

while x > 0:              #whileループを定義して条件式に「xは0より大きい」を指定
    print("{}".format(x)) #書式化文字列に対してformatメソッドを使用して変数xの値に置き換える
    x -= 1                #変数xをディクリメントして再保存

print("Happy New Year!")  #whileループが終了したら出力

# 無限ループ
while True:                #whileループで条件式「True」を定義(永久にTrue評価)
    print("Hello, World!")

# <break>
# breakキーワードでforループを終了
for i in range(0, 100):
    print(i)
    break               #breakキーワードでforループを終了させるポイントを指定

# whileループとbreakを組み合わせたプログラム例
qs = ["What is your name?",
      "What is your fav.color?",
      "What is your quest?"]     #変数qsにリスト型オブジェクトを保存

n = 0                            #変数nに整数型オブジェクトを保存
while True:                      #Whileループで条件式にTrue評価を定義する(=無限ループ)
    print("Type q to quit.")
    a = input(qs[n])             #変数aにinput関数の文字列型オブジェクトの出力値を保存
    if a == "q":
        break                    #if条件式がTrue評価の場合、breakキーワードを使用してWhileループ処理を終了
    n = (n + 1) % 3

# <continue>
# forループとcontinueを組み合わせたプログラム例
for i in range(1, 6):
    if i == 3:
        continue      #if条件式がTrue評価の場合、後に続くプログラムは実行されず次のループ処理を開始する
    print(i)

# whileループとcontinueを組わせたプログラム例
i = 1

while i <= 5:    #whileループで条件式「iが5以下の場合」を定義
    if i == 3:
        i += 1   #if条件式がTrue評価の場合、変数iをインクリメントして再保存
        continue #if条件式がTrue評価の場合、continueキーワードが発動して後に続くプログラムは実行されず、次のループ処理を開始する
    print(i)
    i += 1

# <入れ子のループ(ネストループ)>
# 入れ子のループ例1
for i in range(1, 3):              #変数iにrange関数の整数列(イテラブル)の要素を1つずつ割り当てる(=外側のループ)
    print(i)
    for letter in ["a", "b", "c"]: #変数letterにリスト型オブジェクト(イテラブル)の要素を1つずつ割り当てる(=内側のループ)
        print(letter)

# 入れ子のループ例2
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []           #変数addedに空のリスト型オブジェクトを保存

for i in list1:             #変数iにイテラブルなオブジェクトlist1の要素を1つずつ割り当てる(=外側のループ)
    for j in list2:         #変数jにイテラブルなオブジェクトlist2の要素を1つずつ割り当てる(=内側のループ)
        added.append(i + j) #リスト型オブジェクトaddedに対してappendメソッドを使用して変数iとjの足し算の結果を追加する

print(added)                #全てのforループ処理が終了したらリスト型オブジェクトaddedを出力する

# whileループとforループの入れ子のループ
while input("y or n?") != "n":        #whileループの条件式がTrue評価の間、繰り返し処理を実行する(=外側のループ)
    for i in range(1, 6):             #変数iにrange関数の整数列(イテラブル)の要素を1つずつ割り当てる(=内側のループ)
        print(i)

# <チャレンジ>
# 問題1
shows = ["Thw Walking Dead", "Entourage",
         "The Sopranos", "The Vampire Diaries"] #変数showにリスト型オブジェクト(イテラブル)を保存

for show in shows:                                    #変数showにイテラブルなオブジェクトshowsの要素を1つずつ割り当てる
    print(show)

# 問題2
for i in range(25, 51): #変数iにrange関数の整数列(イテラブル)の要素を1つずつ割り当てる
    print(i)

# 問題3
shows = ["The Walking Dead", "Antourage",
         "The Sopranos", "The Vampire Diaries"] #変数showsにリスト型オブジェクト(イテラブル)を保存

for index, show in enumerate(shows):                  #enumerate関数を使用してイテラブルなオブジェクトshowsのインデックス値と要素を変数indexとshowに一つずつ割り当てる
    print(index)
    print(show)

# 問題4
numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guss a numper or type q to quit!") #変数answerにinput関数の文字列型オブジェクトの出力値を保存

    if answer == "q":
        break                                          #if条件式がTrue評価の場合、breakを使用してwhileループを終了する
    try:                                               #例外が発生する可能性を持つ処理であることを定義
        answer = int(answer)
    except ValueError:                                 #発生する可能性のある例外を定義
        print("please type a number or q to quit!")
        continue                                       #例外が発生した場合、continueを使用して実行中のループ処理を終了して次のループ処理を開始する
    
    if answer in numbers:                              #in演算子を使用して整数型オブジェクトanswerがリスト型オブジェクトnumbersに含まれていることを確認
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

# 問題5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []                  #変数list3に空のリスト型オブジェクトを保存

for i in list1:             #変数iにイテラブルなオブジェクトlist1の要素を1つずつ割り当てる(=外側のループ)
    for j in list2:         #変数jにイテラブルなオブジェクトlist2の要素を1つずつ割り当てる(=内側のループ)
        list3.append(i * j) #リスト型オブジェクトlist3に対してappendメソッドを使用して変数iとjの掛け算の結果を追加する

print(list3)                #全てのforループ処理が終了したらリスト型オブジェクトlist3を出力する