# アルゴリズム

# <FizzBuzz>
for i in range(1,101):                                                                      #整数型オブジェクト1-100をイテラブルなオブジェクトとして１個ずつ変数iに割り当てる
    if i % 3 == 0 and i % 5 == 0:                                                           #if条件式がTrue評価の場合はコードブロックを実行⇒変数iを3で割った余りが0と等価、かつ5で割った余りが0と等価の場合 = 3と5の倍数を調べる！
        print("FizzBuzz")                                                                   #if条件式がTrue評価の場合は「FizzBuzz」と出力
    elif i % 3 == 0:                                                                        #条件式1がFlase評価の場合⇒変数iを3で割った余りが0と等価の場合 = 3の倍数を調べる！
        print("Fizz")                                                                       #条件式2がTrue評価の場合は「Fizz」と出力
    elif i % 5 == 0:                                                                        #条件式1と2がFalse評価の場合⇒変数iを5で割った余りが0と等価の場合 = 5の倍数を調べる！
        print("Buzz")                                                                       #条件式3がTrue評価の場合は「Buzz」と出力
    else:                                                                                   #全ての条件式がFlase評価の場合
        print(i)                                                                            #変数iのデータ(値)を出力

# <線形探索(sequential search)>
def ss(number_list, n):                                                                     #線形探索アルゴリズムの関数を定義
    found = False                                                                           #変数foundにブール型オブジェクトFalseを保存⇒目的のデータ(値)nが見つかったかを判定する！
    for i in number_list:                                                                   #整数型オブジェクト0-99をイテラブルなオブジェクトとして１個ずつ変数iに割り当てる
        if i == n:                                                                          #変数iのデータ(値)が入力値(引数)nと等価の場合はコードブロックを実行
            found = True                                                                    #変数foundにブール型オブジェクトTrueを再保存⇒目的のデータ(値)が見つかったことを記録する！
            break                                                                           #breakキーワードを使用してforループ処理を終了
    return found                                                                            #forループ処理が終了したら変数foundのデータ(値)を出力値(戻り値)として定義

numbers = range(0, 100)                                                                     #変数numbersに整数型オブジェクト0-99を保存
s1 = ss(numbers, 2)                                                                         #変数s1にss関数の出力値(戻り値)を保存⇒検索範囲はnumbers、目的のデータ(値)は2を入力値(引数)として渡す！
print(s1)
s2 = ss(numbers, 202)                                                                       #変数s2にss関数の出力値(戻り値)を保存⇒検索範囲はnumbers, 目的のデータ(値)は202を入力値(引数)として渡す！
print(s2)

# <回文(palindrome)>
def palindrome(word):                                                                       #回文アルゴリズムを定義
    word = word.lower()                                                                     #文字列型オブジェクトwordに対してlowerメソッドを使用⇒大文字を全て小文字に変換する！
    return word[::-1] == word                                                               #逆順にスライスした文字列(word[::-1])と元の文字列(word)が等価の場合⇒等価の場合はTrue評価を出力値(戻り値)として定義する！

print(palindrome("Mother"))
print(palindrome("Mom"))

# <アナグラム(anagram)>
def anagram(w1, w2):                                                                        #アナグラムアルゴリズムを定義
    w1 = w1.lower()                                                                         #文字列型オブジェクトw1に対してlowerメソッドを使用⇒大文字を全て小文字に変換して変数w1に再保存する！
    w2 = w2.lower()                                                                         #文字列型オブジェクトw2に対してlowerメソッドを使用⇒大文字を全て小文字に変換して変数w2に再保存する！
    return sorted(w1) == sorted(w2)                                                         #ソート済文字列(w1, w2)が等価の場合⇒sroted関数でソートした新しい文字列型オブジェクトが等価の場合はTrue評価を出力値(戻り値)として定義する！

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))

# <出現する文字列を数える>
def count_characters(string):                                                               #出現する文字列を数えるアルゴリズム
    count_dict = {}                                                                         #変数count_dictに空の辞書型オブジェクト保存⇒文字列を出現数を記録する容器になる！
    for c in string:                                                                        #入力値(引数)stringをイテラブルなオブジェクトとして１個ずつ変数cに割り当てる
        if c in count_dict:                                                                 #変数cのデータ(値)が辞書型オブジェクトcount_dictのキーに含まれている場合はコードブロックを実行
            count_dict[c] += 1                                                              #if条件式がTrue評価の場合⇒変数cのデータ(値)に該当するキーのバリューをインクリメント
        else:
            count_dict[c] = 1                                                               #if条件式がFalse評価の場合⇒変数Cのデータ(値)を新しいキーバリューペアとして辞書型オブジェクトcount_dictに保存する！
    
    print(count_dict)                                                                       #forループが終了すると辞書型オブジェクトcount_dictを出力

count_characters("Dynasty")

#defaultdict関数を使用して出現する文字列を数える
from collections import defaultdict                                                         #collectionsモジュールからdefautldictメソッドをインポート

def count_characters(string):                                                               #出現する文字列を数えるアルゴリズムを定義
    count_dict = defaultdict(int)                                                           #変数count_dictにdefaultdictメソッドの出力値(戻り値)を保存⇒バリューに規定値(初期値)を設定した辞書型オブジェクトを容器を作成する！
    for c in string:                                                                        #入力値(引数)stringをイテラブルなオブジェクトとして変数cに１個ずつ割り当てる
        count_dict[c] += 1                                                                  #変数cのデータ(値)に該当するキーのバリューをインクリメント⇒辞書型オブジェクトcount_dictに該当するキーが存在しない場合は新しいキーバリューペアが自動的に新しく作成される！
    print(count_dict)                                                                       #forループ処理が終了すると辞書型オブジェクトcount_dictを出力

count_characters("Dynasty")

#Counter関数をして出現する文字列を数える
from collections import Counter                                                             #collectionsモジュールからCounterメソッドをインポート

print(Counter("Dynasty"))                                                                   #Counterメソッドの出力値(戻り値)を出力⇒入力値(引数)Dynastyの要素(オブジェクト)数を集計して辞書型オブジェクトを出力値(戻り値)として定義する
my_dict = Counter("Dynasty")
print(my_dict["y"])                                                                         #辞書型オブジェクトmy_dictのキー「y」のバリューを取得

# <再帰法(recursion)>
def bottles_of_beer(bob):                                                                   #再帰処理を行う関数をで定義
    #ドキュメンテーション文字列
    """ Prints Bottles of Beer on the Wall lyrics.
        :Param bob: Must be a positive integer.
        :Return: String
    """
    #再帰終了条件を設定(無限再帰を防ぐため)
    if bob < 1:                                                                             #入力値(引数)bobのデータ(値)が「1未満」の場合はコードブロックを実行
        print("""\
            No more bottles of beer on the Wall.
            No more bottles of beer.
        """)
        return                                                                              #returnキーワードを使用してbottles_of_beer関数を終了する
    
    tmp = bob                                                                               #変数tmpに入力値(引数)bobのデータ(値)を保存⇒残っているボトル数を記録する！
    #再帰処理が行われる毎に再帰終了条件に近づく(無限再帰を防ぐため)
    bob -= 1                                                                                #入力値(引数)bobをディクリメント⇒ボトル数が1本減る！
    print("""\
        {} bottles of beer in the wall.
        {} bottles of beer.
        Take it down, pass it around.
        {} bottles of beer on the wall.
    """.format(tmp, tmp, bob))                                                              #formatメソッドを使用して書式化文字列を置き換える
    
    #関数が関数自体を呼び出す(再帰終了条件に近づくため)
    bottles_of_beer(bob)                                                                    #関数内でその関数自体を呼び出す(再帰呼び出し)⇒入力値(引数)bobはディクリメントしたデータ(値)を渡す = 再帰終了条件に近づく！

bottles_of_beer(99)

# <チャレンジ>
#問題1