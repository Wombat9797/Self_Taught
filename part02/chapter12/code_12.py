# プログラミングパラダイム

# <手続き型プログラミング>
pop = []
jpop = []                                                 #変数popとjpopに空のリスト型オブジェクトを保存(=グローバルステートの変数)

def collect_songs():
    ask = "pかjのどちらかを入力してください。qで終わります。"
    song = "曲名を入力してください:"

    while True:                                           #whileループ処理⇒条件式にブール型オブジェクトTrueを指定して無限ループを定義
        genere = input(ask)                               #変数henereにinput関数の文字列型オブジェクトの出力値を保存

        if genere == "q":                                 #if条件式⇒文字列型オブジェクトgenereの値が「q」と等価の場合
            break                                         #breakキーワード⇒whileループ全体を終了

        if genere == "p":                                 #if条件式⇒文字列型オブジェクトgenereの値が「p」と等価の場合
            p = input(song)                               #変数pにinput関数の文字列型オブジェクトの出力値(曲名)を保存
            pop.append(p)                                 #リスト型オブジェクトpopに対してappendメソッドを使用して文字列型オブジェクトpの値を追加
        
        elif genere == "j":                               #elif条件式⇒文字列型オブジェクトgenereの値が「j」と等価の場合
            j = input(song)                               #変数jにinput関数の文字列型オブジェクトの出力値(曲名)を保存
            jpop.append(j)                                #リスト型オブジェクトjpopに対してappendメソッドを使用して文字列型オブジェクトpの値(曲名)を追加
        
        else:                                             #else⇒ifとelifの条件式が「False」の場合
            print("不正な値です。")
    
    print("pop songs: ", pop)                             #popリストを出力
    print("jpop songs: ", jpop)                           #jpopリストを出力

collect_songs()

# <関数型プログラミング>
# 手続き型プログラミングの問題点
a = 0

def increment():
    global a                                              #globalキーワード⇒グローバルステートの変数aを操作することを明示的に指定
    a +=1                                                 #グローバルステートの変数aをインクリメント
    print(a)

increment()

# <関数型プログラミング>
def increment(a):                                         #グローバルステートを使用しないで、インクリメントを実行(=予期しない変更を防ぐ)
    return a + 1

print(increment(1))

# <オブジェクト指向型プログラミング>
# クラスの定義
class Orange:                                             #Orangeクラスを定義
    def __init__(self):                                   #特殊メソッドを定義
        print("created!")

# インスタンス変数の定義
class Orange:                                             #Orangeクラスを定義
    def __init__(self, w, c):                             #特殊メソッドを定義
        self.weight = w                                   #インスタンス変数wightに入力値「W」の値を保存
        self.color = c                                    #インスタンス変数cに入力値「c」の値を保存
        print("created!")

# クラスからインスタンス(オブジェクト)を作成
class Orange:                                             #Orangeクラスを定義
    def __init__(self, w, c):                             #特殊メソッドを定義(=オブジェクトを作成するためのメソッド)
        self.wight = w                                    #インスタンス変数wightに入力値(引数)「w」のデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)「c」のデータ(値)を保存
        print("created!")

or1 = Orange(10, "dark orange")                           #Orangeクラスを使用してインスタンス(オブジェクト)を作成して変数or1に保存＝クラスのインスタンス化
print(or1)

# インスタンス変数の値を取得
class Orange:                                             #Orangeクラスを定義
    def __init__(self, w, c):                             #特殊メソッドを定義(=オブジェクトを作成する目的で使用)
        self.wight = w                                    #インスタンス変数wightに入力値(引数)「w」のデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)「c」のデータ(値)を保存
        print("instance created!!")

or1 = Orange(10, "dark orange")                           #Orangeクラスの特殊メソッドを使用してインスタンス(オブジェクト)を作成して、変数or1に保存
print(or1.wight)                                          #Orangeクラスのインスタンス(オブジェクト)or1のインスタンス変数wightのデータ(値)を取得
print(or1.color)                                          #Orangeクラスのインスタンス(オブジェクト)or1のインスタンス変数colorのデータ(値)を取得

# インスタンス変数のデータ(値)を変更
class Orange:                                             #orangeクラスを定義
    def __init__(self, w, c):                             #インスタンスを生成する特殊メソッドを定義
        self.weight = w                                   #インスタンス変数weightに入力値(引数)のデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)のデータ(値)を保存
        print("created")

or1 = Orange(10, "dark orange")                           #Orangeクラスを使用してインスタンスを生成して変数or1に保存
print(or1.weight)                                         #Orangeクラスのインスタンスor1のインスタンス変数のデータ(値)を取得
print(or1.color)                                          #Orangeクラスのインスタンスor1のインスタンス変数のデータ(値)を取得

or1.weight = 100                                          #Orangeクラスのインスタンスor1のインスタンス変数weightに整数型オブジェクト100を再保存
or1.color = "light orange"                                #Orangeクラスのインスタンスor1のインスタンス変数colorに文字列型オブジェクトlight orangeを再保存
print(or1.weight)                                         #Orangeクラスのインスタンスor1のインスタンス変数wightのデータ(値)を取得
print(or1.color)                                          #Orangeクラスのインスタンスor1のインスタンス変数colorのデータ(値)を取得

# 複数のインスタンス(オブジェクト)を作成
class Orange:                                             #Orangeクラスを定義
    def __init__(self, w, c):                             #インスタンス(オブジェクト)を生成する特殊メソッドを定義
        self.weight = w                                   #インスタンス変数weightに入力値(引数)wのデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)cのデータ(値)を保存
        print("created!")

or1 = Orange(4, "light orange")                           #Orangeクラスを使用してインスタンス(オブジェクト)を作成して変数or1に保存
or2 = Orange(8, "dark orange")                            #同上、変数or2に保存
or3 = Orange(14, "yellow")                                #同上、変数or3に保存
                                                          #Orangeクラスを使用して異なるデータ(値)を保持する3つのインスタンス(オブジェクト)を作成している

# 新しい属性をクラスに追加
class Orange:                                             #Orangeクラスを定義
    def __init__(self, w, c):                             #インスタンスを生成する特殊メソッドを定義
        """weight(重さ)はグラム"""
        self.weight = w                                   #インスタンス変数weightに入力値(引数)wのデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)cのデータ(値)を保存
        self.mold = 0                                     #インスタンス変数moldに整数型オブジェクト0を保存
        print("created!")
    
    def rot(self, days, temp):                            #新しいメソッドを定義
        """temp(温度)は摂氏"""
        self.mold = days * temp                           #入力値(引数)daysとtempを掛けたデータ(値)をインスタンス変数moldに再保存(⇒インスタンス変数はクラス内のメソッドで利用できる)

orange = Orange(200, "orange")                            #Orangeクラスを使用してインスタンス(オブジェクト)を作成して変数orangeに保存
print(orange.mold)                                        #Orangeクラスのインスタンス(オブジェクト)のインスタンス変数のデータ(値)を取得
orange.rot(10, 37)                                        #orangeインスタンス(オブジェクト)を使用してOrangeクラスのrotメソッドを呼び出す
print(orange.mold)                                        #Orangeクラスのインスタンス(オブジェクト)のインスタンス変数moldのデータ(値)を取得

# メソッドでインスタンス変数を変更
class Rectangle:                                          #Rectangleクラスを定義
    def __init__(self, w, l):                             #オブジェクト(インスタンス)作成の為の特殊メソッドを定義
        self.width = w                                    #インスタンス変数widthに入力値(引数)wのデータ(値)を保存
        self.len = l                                      #インスタンス変数lenに入力値(引数)lのデータ(値)を保存
    
    def area(self):                                       #areaメソッドを定義
        return self.width * self.len                      #インスタンス変数widthとlenの積を出力値(戻り値)として定義
    
    def change_size(self, w, l):                          #change_sizeメソッドを定義
        self.width = w                                    #インスタンス変数widthに入力値(引数)wのデータ(値)を再保存
        self.len = l                                      #インスタンス変数lenに入力値(引数)lのデータ(値)を再保存

rectangle = Rectangle(10, 20)                             #Rectangleクラスを特殊メソッドを使用してオブジェクト(インスタンス)を作成して変数rectangleに保存
print(rectangle.area())                                   #rectangleオブジェクト(インスタンス)を使用してareaメソッドを呼び出す

rectangle.change_size(20, 40)                             #rectangleオブジェクト(インスタンス)を使用してchange_sizeメソッドを呼び出す
print(rectangle.area())                                   #rectangleオブジェクト(インスタンス)を使用してareaメソッドを呼び出す

# <チャレンジ>
# 問題1
class Apple:                                              #Appleクラスを定義
    def __init__(self, w, c, n, a):                       #オブジェクト(インスタンス)を作成する特殊メソッドを定義
        self.weight = w                                   #インスタンス変数wightに入力値(引数)wのデータ(値)を保存
        self.color = c                                    #インスタンス変数colorに入力値(引数)cのデータ(値)を保存
        self.name = n                                     #インスタンス変数nameに入力値(引数)nのデータ(値)を保存
        self.area = a                                     #インスタンス変数areaに入力値(引数)aのデータ(値)を保存
    
    def apple_print(self):
        return "{}gの{}色の{}産の{}を貰った!".format(self.weight, self.color, self.area, self.name)

apple = Apple(100, "Red", "Fuji", "Aomori")               #Appleクラスの特殊メソッドを使用してオブジェクト(インスタンス)を作成して変数appleに保存
print(apple.apple_print())                                #appleオブジェクトを使用してapple_printメソッドを呼び出す

# 問題2
import math                                               #mathモジュールをインポート

class Circle:                                             #Circleクラスを定義
    def __init__(self, r):                                #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.radius = r                                   #インスタンス変数radiusに入力値(引数)のデータ(値)を保存
    
    def area(self):                                       #円の面積を求めるareaメソッドを定義
        return self.radius * self.radius * math.pi        #円の面積を出力値(戻り値)として定義

circle = Circle(5)                                        #Circleクラスの特殊メソッドを使用してオブジェクト(インスタンス)を作成して変数circleに保存
print(circle.area())                                      #circleオブジェクト(インスタンス)を使用してareaメソッドを呼び出す

# 問題3
class Triangle:                                           #Triangleクラスを定義
    def __init__(self, b, h):                             #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.bottom = b                                   #インスタンス変数bottomに入力値(引数)bのデータ(値)を保存
        self.height = h                                   #インスタンス変数heightに入力値(引数)hのデータ(値)を保存
    
    def area(self):                                       #三角形の面積を計算するareaメソッドを定義
        return self.bottom * self.height / 2              #計算結果を出力値(戻り値)として定義

triangle = Triangle(10, 5)                                #Triangelクラスの特殊メソッドを使用してオブジェクト(インスタンス)を作成して変数triangleに保存
print(triangle.area())                                    #triangleオブジェクト(インスタンス)を使用してareaメソッドを呼び出す

# 問題4
class Hexagon:                                            #Hexagonクラスを定義
    def __init__(self, r):                                #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.corner = 6                                   #インスタンス変数cornerに角の数6を保存
        self.radius = r                                   #インスタンス変数radiusに入力値(引数)rのデータ(値)を保存
    
    def calcurate_perimeter(self):                        #６角形の外周を計算するメソッドを定義
        return self.corner * self.radius                  #計算結果を出力値(戻り値)として定義

hexagon = Hexagon(10)                                     #Hexagonクラスを使用してオブジェクト(インスタンス)を作成して変数hexagonに保存
print(hexagon.calcurate_perimeter())                      #hexagonオブジェクト(インスタンス)を使用してcalcurate_perimeterメソッドを呼び出す

# <チャレンジ_解答例>
# 問題1
class Apple:                                              #Appleクラスを定義
    def __init__(self, color, weight, stem, circum):      #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.color = color                                #インスタンス変数colorに入力値(引数)colorのデータ(値)を保存
        self.weight = weight                              #インスタンス変数weightに入力値(引数)weightのデータ(値)を保存
        self.stem_length = stem                           #インスタンス変数stem_lenghtに入力値(引数)stemのデータ(値)を保存
        self.circumference = circum                       #インスタンス変数circumferenceに入力値(引数)circumのデータ(値)を保存

    def apple_print(self):                                #メソッドを定義
        return "そのリンゴの色は{}, 重さは{}g, 茎の長さは{}cm, 外周は{}cmです!".format(self.color, self.weight, self.stem_length, self.circumference)

apple = Apple("赤", 100, 10, 15)                          #Appleクラスを使用してオブジェクト(インスタンス)を作成して変数appleに保存
print(apple.apple_print())                                #appleオブジェクト(インスタンス)を使用してapple_printメソッドを呼び出す

# 問題2
import math                                               #mathモジュールをインポート

class Circle:                                             #Circleクラスを定義
    def __init__(self, radius):                           #オブジェクト(インスタンス)を作成するための特殊メソッドを定義
        self.radius = radius                              #インスタンス変数radiusに入力値(引数)radiusのデータ(値)を保存
    
    def calculate_area(self):                             #円の面積を計算するメソッドを定義
        return self.radius ** 2 * math.pi                 #計算結果を出力値(戻り値)として定義

area_circle = Circle(4)                                   #Circleクラスを使用してオブジェクト(インスタンス)を作成して変数area_circleに保存
print(area_circle.calculate_area())                       #area_circleオブジェクト(インスタンス)を使用してcalculate_areaメソッドを呼び出す

# 問題3
class Triangle:                                           #Triangleクラスを定義
    def __init__(self, base, height):                     #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.base = base                                  #インスタンス変数baseに入力値(引数)のデータ(値)を保存
        self.height = height                              #インスタンス変数heightに入力値(引数)でデータ(値)を保存
    
    def calculate_area(self):                             #三角形の面積を求めるメソッドを定義
        return self.base * self.height / 2                #計算結果を出力値(戻り値)として定義

area_triangle = Triangle(20, 30)                          #Triangleクラスを使用してオブジェクト(インスタンス)を作成して変数area_triangleに保存
print(area_triangle.calculate_area())                     #area_triangleオブジェクト(インスタンス)を使用してcalculate_areaメソッドを呼び出す

# 問題4
class Hexagon:                                            #Hexagonクラスを定義
    def __init__(self, s1, s2, s3, s4, s5, s6):           #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.s1 = s1                                      #インスタンス変数s1-s6に入力値(引数)s1-s6のデータ(値)を保存
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    
    def calculate_perimeter(self):                        #6角形の外周を計算するメソッドを定義
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

p_hexagon = Hexagon(1, 2, 3, 4, 5, 6)                     #Hexagonクラスを使用してオブジェクト(インスタンス)を作成して変数p_hexagonに保存
print(p_hexagon.calculate_perimeter())                    #p_hexagonオブジェクト(インスタンス)を使用してcalculate_perimeterメソッドを呼び出す