# コンテナ

# <メソッド>
# メソッドの例
"Hello".upper()           #文字列型オブジェクトHelloに対してupperメソッドを使用する
"Hello".replace("o", "@") #同上に対してreplaceメソッドを使用する

# <リスト>
# リストの定義
fruit = list() #list関数を使用して空のリスト型オブジェクトを変数fruitに保存
fruit

fruit = []     #角カッコ([])を使用して空のリスト型オブジェクトを変数fruitに保存
fruit

# オブジェクトを保存したリストを定義
fruit = ["Apple", "Orange", "Pear"] #変数fruitに文字列型オブジェクトを保存したリスト型オブジェクトを保存
fruit

# リストに新しいオブジェクト(要素)を追加
fruit = ["Apple", "Orange", "Pear"]
print(fruit)

fruit.append("Banana")              #リスト型オブジェクトfruitに対してappendメソッドを使用して文字列型オブジェクトBananaを追加
fruit.append("Peach")               #リスト型オブジェクトfruitに対してappendメソッドを使用して文字列型オブジェクトPeachを追加
print(fruit)

# リストに保存できるオブジェクトの種類
random = []
print(random)

random.append(True)    #リスト型オブジェクトrandomに対してappendメソッドを使用してブール型オブジェクトTrueを追加
random.append(100)     #同上に整数型オブジェクト100を追加
random.append(1.1)     #同上に浮動小数点数型オブジェクト1.1を追加
random.append("Hello") #同上に文字列型オブジェクトHelloを追加
print(random)

# インデックスを指定してオブジェクト(要素)を取得
fruit = ["Apple", "Orange", "Pear"]
print(fruit[0])                     #リスト型オブジェクトfruitのインデックス「0」の要素を取得
print(fruit[1])                     #同上のインデックス「1」の要素を取得
print(fruit[2])                     #同上のインデックス「2」の要素を取得

# 存在しないインデックスを指定した場合
colors = ["blue", "green", "yellow"]
colors[4]                            #インデックス「4」は存在しないので例外(IndexError)が発生する

# オブジェクト(要素)を変更
colors = ["blue", "green", "yellow"]
print(colors)

colors[2] = "red"                 #リスト型オブジェクトcolorsのインデックス「2」の要素に文字列型オブジェクトredを再保存
print(colors)

# オブジェクト(要素)を削除
colors = ["blue", "green", "yellow"]
print(colors)

colors.pop()                         #リスト型オブジェクトcolorsに対してpopメソッドを使用して末尾の要素を削除する
print(colors)

# 空のリスト型オブジェクトにpopメソッドを使用した場合
colors = []
colors.pop()  #空のリスト型オブジェクトに対してpopメソッドを使用した場合は例外(IndexError)が発生する
print(colors)

# リストを連結
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
colors1 + colors2                     #加算演算子(+)を使用してリスト型オブジェクトcolors1・colors2を連結する

# オブジェクト(要素)がリストに含まれているか確認
colors = ["blue", "green", "yellow"]
"green" in colors                    #in演算子を使用して文字列型オブジェクトgreenがリスト型オブジェクトcolorsに含まれているか確認する

# オブジェクト(要素)がリストに含まれていないことを確認
colors = ["blue", "green", "yellow"]
"balck" not in colors                #not in演算子を使用して文字列型オブジェクトblackがリスト型オブジェクトcolorsに含まれていないことを確認する

# 保存されているオブジェクト(要素)の数を取得
colors = ["blue", "green", "yellow"]
len(colors)                          #len関数を使用してリスト型オブジェクトcolorsの中に保存されているオブジェクト(要素)の数を取得する

# リストを使用したプログラム例
colors = ["purple", "orange", "green"] #変数colorsにリスト型オブジェクトを保存

guess = input("何色でしょう？(入力してください): ") #変数guessにinput関数の文字列型オブジェクト出力値を保存

if guess in colors:                              #in演算子を使用して文字列型オブジェクトguessがリスト型オブジェクトcolorsに含まれているか確認する
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")

# <タプル>
# タプルの定義
my_tuple = tuple() #tuple関数を使用して変数my_tupleに空のタプル型オブジェクトを保存
my_tuple

my_tuple = ()      #丸カッコを使用して変数my_tupleに空のタプル型オブジェクトを保存
my_tuple

# タプル作成時にオブジェクト(要素)を追加
rndm = ("M. Jackson", 1958, True)
rndm

# タプル作成時にオブジェクト(要素)を追加する時の注意点
my_tuple = ("self_tought",)
print(my_tuple)             #タプルの括弧と認識される

my_sum = (9 + 1) * 10
print(my_sum)               #数値演算の括弧と認識される

# タプルのオブジェクト(要素)を変更した場合
dys = ("1984", "Brave New World", "Fahrenheit 451")
dys[1] = "Handmaid's Tale"                          #タプル型オブジェクトはイミュータブルなので、要素を変更・追加・削除しようとすると例外(TypeError)が発生する

# インデックスを指定して保存されたオブジェクト(要素)を取得
dys = ("1984", "Brave New World","Fahrenheit 451")
dys[2]                                             #タプル型オブジェクトdysのインデックス「2」の要素を取得

# オブジェクト(要素)がタプルに含まれているか確認
dys = ("1984", "Brave New World", "Fahrenheit 451")
"1984" in dys                                       #in演算子を使用して文字列型オブジェクト1984がタプル型オブジェクトdysに含まれているか確認する

# オブジェクト(要素)がタプルに含まれていないことを確認
dys = ("1984", "Brave New World", "Fahrenheit 451")
"Handmaid's Tale" not in dys                        #not in演算子を使用して文字列型オブジェクトHandmaid's Taleがタプル型オブジェクトdysに含まれていないことを確認する

# <辞書>
# 辞書の定義
my_dict = dict() #dict関数を使用して変数my_dictに空の辞書型オブジェクトを保存
print(my_dict)

my_dict = {}     #波カッコ({})を使用して変数my_dictに空の辞書型オブジェクトを保存
print(my_dict)

# 辞書作成時にキーバリューペアを追加
fruit = {"Apple": "red",
            "Banana": "yellow"} #変数fruitに辞書型オブジェクトを保存
fruit

#キーバリューペアを追加
facts = dict()
print(facts)

facts["code"] = ["fun"]   #辞書型オブジェクトfactsにキー「code」を追加してバリュー「fun」と関連付ける
facts["Bill"] = ["Gates"] #辞書型オブジェクトfactsにキー「Bill」を追加してバリュー「Gates」と関連付ける
facts["founded"] = [1776] #辞書型オブジェクトfatcsにキー「founded」を追加してバリュー「1776」と関連付ける

print(facts)
print(facts["code"])      #辞書型オブジェクトfatsのキー「code」のバリューを取得する
print(facts["Bill"])      #辞書型オブジェクトfatcsのキー「Bill」のバリューを取得する
print(facts["founded"])   #辞書型オブジェクトfactsのキー「founded」のバリューを取得する
print(facts["Bill Doors"]) #存在しないキーのバリューを取得しようとすると例外(KeyError)が発生する

# キーが辞書に含まれていることを確認
bill = {"Bill Gates": "charitable"}

"Bill Gates" in bill                #in演算子を使用して文字列型オブジェクトBill Gatesが辞書型オブジェクトbillのキーに含まれていることを確認

# キーが辞書に含まれていないことを確認
bill = {"Bill Gates": "charitable"}

"Bill Doors" not in bill            #not in演算子を使用して文字列型オブジェクトBill Doorsが辞書型オブジェクトbillのキーに含まれていないことを確認

# キーバリューペアを削除
books = {"Dracula": "Stocker",
         "1984": "Orwell",
         "The Trial": "Kafka"}
print(books)

del books["The Trial"]         #delキーワードを使用して辞書型オブジェクトbooksから「The Trial」のキーバリューペアを削除する
print(books)

# 辞書を使用したプログラム例
songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"}  #変数songsに辞書型オブジェクトを保存

n = input("数字を入力してください: ") #変数nにinput関数の文字列型オブジェクト出力値を保存

if n in songs:                      #変数nに保存された値が辞書型オブジェクトsongsのキーに含まれていることを確認
    song = songs[n]                 #条件式がTrue評価の場合、変数nに該当するキーのバリューを変数songに保存
    print(song)
else:
    print("見つかりません。")

# <コンテナの中のコンテナ>
# リストの中にオブジェクト(要素)としてリストを保存
lists = []
print(lists)

rap = ["カニエ・ウェスト", "ジェイ・z", "エミネム", "ナズ"]        #変数rapにリスト型オブジェクトを保存
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・チェッペリン"] #変数rockに同上
djs = ["ゼッズ・デッド", "ティエスト"]                            #変数djsに同上

lists.append(rap)                                               #リスト型オブジェクトlistsに対してappendメソッドを使用してリスト型オブジェクトrapを追加
lists.append(rock)                                              #同上、リスト型オブジェクトrockを追加
lists.append(djs)                                               #同上、リスト型オブジェクトdjsを追加

print(lists)

rap = lists[0]                                                  #変数rapにリスト型オブジェクトlistsのインデックス「0」のオブジェクト(要素)を再保存
print(rap)

rap = lists[0]                                                  #変数rapにリスト型オブジェクトlistsのインデックス「0」のオブジェクト(要素)を再保存
rap.append("ケンドリック・ラマー")                                #リスト型オブジェクトrapに対してappendメソッドを使用して文字列型オブジェクトを追加
print(rap)
print(lists)

# リストの中にオブジェクト(要素)としてタプルを保存
locations = []

la = (34.0522, 188.2437)     #変数laにタプル型オブジェクトを保存
chicago = (41.8781, 87.6298) #変数chicagoにタプル型オブジェクトを保存

locations.append(la)         #リスト型オブジェクトlocationsに対してappendメソッドを使用してタプル型オブジェクトlaを追加
locations.append(chicago)    #同上、タプル型オブジェクトchicagoを保存

print(locations)

# タプルのオブジェクト(要素)としてリストを保存
eights = ["Edgar Allan Poe", "Charles Dicknes"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)                       #変数authorsにリスト型オブジェクトを保存したタプル型オブジェクトを保存
print(authors)

# リストとタプルのオブジェクト(要素)として辞書を保存
bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]                   #変数my_listに辞書型オブジェクトbdayを保存したリスト型オブジェクトを保存
print(my_list)

my_tuple = (bday,)                  #変数my_tupleに辞書型オブジェクトbdayを保存したタプル型オブジェクトを保存
print(my_tuple)

# 辞書のバリューにリスト・タプル・辞書を保存
ny = {
    "座標": (40.7128, 74.0059),                                    #キー「座標」のバリューにタプル型オブジェクトを保存
    "セレブ": ["ウッディ・アレン", "ジェイ・z", "ケヴィン・ベーコン"], #キー「セレブ」のバリューにリスト型オブジェクトを保存
    "事実": {"州": "ニューヨーク", "国": "アメリカ"}                 #キー「事実」のバリューに辞書型オブジェクトを保存
}

print(ny)

# <チャレンジ>
# 問題1
fav_musicians = ["Linkin Park", "Armin Van Buuren", "Zedd"] #変数musicianにリスト型オブジェクトを保存
fav_musicians

# 問題2
locations = [(33.95, 151.17), (41.38, 2.17), (25.03, 121.63)] #変数locationsにタプル型オブジェクトが保存されたリスト型オブジェクトを保存
locations

# 問題3
me = {"name": "Yuto Nishime",
      "height": 176.0,
      "eyecolor": "Balck",
      "fav_suthor": "Hemingway"} #変数meに辞書型オブジェクトを保存
me

# 問題4
me = {"name": "Yuto Nishime",
      "height": 176.0,
      "eyecolor": "Black",
      "fav_author": "Hemingway"}                              #変数meに辞書型オブジェクトを保存

answer = input("type name, height, eyecolor or fav_author: ") #変数answerにinput関数の文字列型オブジェクト出力値を保存

if answer in me:                                              #in演算子を使用して変数answerに保存された値が辞書型オブジェクトmeのキーに含まれていることを確認
    result = me[answer]                                       #条件式がTrue評価の場合、変数answerの値に該当するキーのバリューを変数resultに保存
    print(result)
else:
    print("Invalid key!")

# 問題5
songs = {"Linkin Park": ["Faint", "Numb", "Bleed it out"],
         "Armin Van Buuren": ["In and out of Love", "Beautiful Life", "Ping Pong"],
         "Zedd": ["Beautiful Now", "The Middle", "Clarity"]}                        #変数fav_musicianに辞書型オブジェクトを保存