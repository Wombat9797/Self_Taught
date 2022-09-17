# ファイル

# <ファイルに書き出す＆ファイルから読み込む>
# ファイルパスを組み立てる
import os
os.path.join("Users", "bob", "st.txt") #osモジュールのpath.join関数を呼び出して入力値(引数)に文字列型オブジェクトのフォルダ・ファイル名を渡す

# ファイルを開く・書き込む・閉じる
st = open("st.txt", "w", encoding="utf-8") #変数stにopen関数のファイル型オブジェクトの出力値を保存
st.write("Hi from Python!")                #ファイル型オブジェクトstに対してwriteメソッドを使用して文字列型オブジェクトを書き込む
st.close()                                 #同上、closeメソッドを使用してファイルを閉じる

# <ファイルを自動的に閉じる>
with open("sts.txt", "w", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトの出力値を保存
    f.write("Hi from Python!!")                   #ファイル型オブジェクトfに対してwriteメソッドを使用して文字列型オブジェクトを書き込む
                                                  #with文のコードブロックが終了すると自動的にファイルを閉じる

# ファイルを開く・読み込む・閉じる
with open("sts.txt", "r", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトの出力値を保存
    print(f.read())                               #ファイル型オブジェクトfに対してreadメソッドを使用して、ファイル内に含まれる全てのイテラブルなオブジェクトを取り出す
                                                  #with文のコードブロックが終了すると自動的にファイルを閉じる

# 読み込んだファイルデータを保存
my_list = []

with open("sts.txt", "r", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトの出力値を保存
    my_list.append(f.read())                      #リスト型オブジェクトmy_listに対してappendメソッドを使用してreadメソッドで取り出したイテラブルなオブジェクトを追加する
                                                  #with文のコードブロックが終了すると自動的にファイルを閉じる
print(my_list)

# <csv>
# csvファイルを書き出す
import csv

with open("stst.csv", "w", newline="", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトの出力値を保存
    w = csv.writer(f, delimiter=",")               #csvモジュールのwriterメソッドを使用してcsv型オブジェクトに変換するファイル型オブジェクトとデリミタを指定して変数wに保存
    w.writerow(["one", "two", "three"])            #csv型オブジェクトに対してwriterowメソッドを使用してリスト型オブジェクトの要素を書き出す
    w.writerow(["four", "five", "six"])            #csv型オブジェクトに対してwriterowメソッドを使用してリスト型オブジェクトの要素を書き出す
                                                   #with文のコードブロックが終了すると自動的にファイルを閉じる

# csvファイルを読み込む
import csv

#⇒ファイルの書き出し部分
with open("ststs.csv", "w", newline="", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトを保存
    w = csv.writer(f, delimiter=",")                            #csvモジュールのwriterメソッドを使用してcsv型オブジェクトに変換するファイル型オブジェクトfとデリミタ(,)を指定して変数wに保存する
    w.writerow(["one", "two", "three"])                         #csv型オブジェクトwに対してwriterowメソッドを使用してリスト型オブジェクトの要素を書き出す
    w.writerow(["four", "five", "six"])                         #csv型オブジェクトwに対してwriterowメソッドを使用してリスト型オブジェクトの要素を書き出す
                                                                #with文のコードブロックが終了すると自動的にファイルを閉じる

#⇒ファイルの読み込み部分
with open("ststs.csv", "r", encoding="utf-8") as f: #変数fにopen関数のファイル型オブジェクトの出力値を保存
    r = csv.reader(f, delimiter=",")                #csvモジュールのreaderメソッドを使用してファイル型オブジェクトfの要素を行単位(イテラブル)で取得する
    for row in r:                                   #変数rowに行単位で取得したイテラブルrの要素を1つずつ割り当てる
        print(",".join(row))                        #joinメソッドを使用して変数rowに割り当てられた要素の間に「,」を追加する
                                                    #with文のコードブロックが終了すると自動的にファイルを閉じる

# <チャレンジ>
# 問題1
with open("qs1.txt", "w", encoding="utf-8") as f: #変数fにopen関数の書き出し専用のファイル型オブジェクトの出力値を保存
    w = f.write("Hello from Python!!")            #ファイル型オブジェクトfに対してwriteメソッドを使用して文字列型オブジェクトを書き出して変数wに保存

with open("qs1.txt", "r", encoding="utf-8") as f: #変数fにopen関数の読み込み専用のファイル型オブジェクトの出力値を保存
    r = f.read()                                  #読み込み専用のファイル型オブジェクトfに対してreadメソッドを使用して全てのイテラブルのオブジェクトを読み込んで変数rに保存
    print(r)                                      #with文のコードブロックが終了すると自動的にファイルを閉じる

# 問題2
answer = input("What is your favorite color!?") #変数answerにinput関数の文字列型オブジェクトの出力値を保存

with open("qs2.txt", "w", encoding="utf-8") as f: #変数fにopen関数の読み書き両方できるファイル型オブジェクトの出力値を保存
    w = f.write(answer)                            #読み書き両方できるファイル型オブジェクトfに対してwriteメソッドを使用して文字列型オブジェクトanswerの値を書き出す
    w = f.read()                                   #読み書き両方できるファイル型オブジェクトfに対してreadメソッドを使用してイテラブルなオブジェクトを読み込で変数rに保存
                                                   #with文のコードブロックが終了すると自動的にファイルを閉じる

# 問題3
import csv #csvモジュールをインポート

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]       #変数moviesにリスト型オブジェクトを保存

with open("qs3.csv", "w", encoding="utf-8", newline="") as csvfile: #変数csvfileにopen関数の書き出し専用のファイル型オブジェクトを保存
    spamwriter = csv.writer(csvfile, delimiter=",")                 #書き出し専用のファイル型オブジェクトcsvfileをcsvモジュールのwriterメソッドを使用してcsv型オブジェクトに変換して変数spamwriterに保存
    for movie_list in movies:                                       #変数movie_listにイテラブルなオブジェクトmoviesの要素を1つずつ割り当てる
        spamwriter.writerow(movie_list)                             #csv型オブジェクトspamwriterに対してwriterowメソッドを使用して変数movie_listに割り当てられたリスト型オブジェクトを1行ずつ書き出す

#問題4
import csv #csvモジュールをインポート

movies = [["トップ・ガン", "リスキー・ビジネス", "マイノリティ・リポート"],
          ["タイタニック", "ザ・レヴェナント", "インセプション"],
          ["トレーニング・デイ", "マン・オン・ファイア", "フライト"]]       #変数moviesにリスト型オブジェクトを保存

with open("qs4.csv", "w", encoding="utf-8", newline="") as csvfile:     #変数csvfileにopen関数の書き出し専用のファイル型オブジェクトを保存
    spamwriter = csv.writer(csvfile, delimiter=",")                     #書き出し専用のファイル型オブジェクトcsvfileをcsvモジュールのwriterメソッドを使用してcsv型オブジェクトに変換して変数spamwriterに保存
    for movie_list in movies:                                           #変数movie_listにイテラブルなオブジェクトmoviesの要素を1つずつ割り当てる
        spamwriter.writerow(movie_list)                                 #csv型オブジェクトspamwriterに対してwriterowメソッドを使用して変数movie_listに割り当てられたリスト型オブジェクトを1行ずつ書き出す