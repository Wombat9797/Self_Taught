# もっとオブジェクト指向型プログラミング

# <クラスオブジェクト>
# クラスオブジェクトを作成
class Square:                                                              #Squareクラスを定義
    pass

print(Square)

# <クラス変数 vs インスタンス変数>
# インスタンス変数の例
class Rectangle():                                                         #Rectangleクラスを定義
    def __init__(self, w, l):                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.width = w                                                     #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒パブリック変数
        self.len = l                                                       #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒パブリック変数
    
    def print_size(self):                                                  #パブリックメソッドを定義
        print("{} by {}!".format(self.width, self.len))                    #formatメソッドを使用して書式化文字列をインスタンス変数widthとlenに置き換える

my_rectangle = Rectangle(10, 24)                                           #Rectangleクラスを使用してインスタンスオブジェクトを作成して変数my_rectangleに保存
my_rectangle.print_size()                                                  #my_rectangleインスタンスオブジェクトを通してprint_sizeメソッドを呼び出す

# クラス変数
class Rectangle():                                                         #Rectangleクラスを定義
    recs = []                                                              #クラス変数recsに空のリスト型オブジェクトを保存⇒クラスオブジェクトとインスタンスオブジェクトから参照できる

    def __init__(self, w, l):                                              #インスタンスオブジェクトを作成する為に特殊メソッドを定義
        self.width = w                                                     #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒パブリック変数
        self.len = l                                                       #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒パブリック変数
        self.recs.append((self.width, self.len))                           #クラス変数recsに対してappendメソッドを使用してインスタンス変数widthとlenのデータ(値)をタプル型オブジェクトとして追加
    
    def print_size(self):                                                  #パブリックメソッドを定義
        print("{} by {}!".format(self.width,self.len))                     #formatメソッドを使用して書式化文字列をインスタンス変数widthとlenに置き換える

r1 = Rectangle(10, 24)                                                     #Rectangleクラスを使用してインスタンスオブジェクトを作成して変数r1に保存
print(r1.recs)                                                             #r1インスタンスオブジェクトを通してクラス変数recsを取得
r1.print_size()                                                            #r1インスタンスオブジェクトを通してprint_sizeメソッドを呼び出す

r2 = Rectangle(20, 40)                                                     #Rectangleクラスを使用してインスタンスオブジェクトを作成して変数r2に保存
print(r2.recs)                                                             #r2インスタンスオブジェクトを通してクラス変数recを取得
r2.print_size()                                                            #r2インスタンスオブジェクトを通してprint_sizeメソッドを呼び出す

r3 = Rectangle(100, 200)                                                   #Rectangleクラスを使用してインスタンスオブジェクトを作成して変数r3に保存
print(r3.recs)                                                             #r3インスタンスオブジェクトを通してクラス変数recsを取得
r3.print_size()                                                            #r3インスタンスオブジェクトを通してprint_sizeメソッドを呼び出す

print(Rectangle.recs)                                                      #Rectangleクラスを通してクラス変数を取得

# <特殊メソッド>
# インスタンスオブジェクトを出力した場合
class Lion():                                                              #Lionクラスを定義⇒objectクラスを継承している
    def __init__(self, name):                                              #インスタンスオブジェクトを作成する為に特殊メソッドを定義
        self.name = name                                                   #インスタンス変数nameに入力値(引数)のデータ(値)を保存⇒パブリック変数

lion = Lion("Gilbert")                                                     #Lionクラスを使用してインスタンスオブジェクトを作成して変数lionに保存
print(lion)                                                                #lionインスタンスオブジェクトを出力する

# objectクラスの__repr__特殊メソッドをオーバーライドした場合
class Lion():                                                              #Lionクラスを定義⇒objectクラスを継承している
    def __init__(self, name):                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.name = name                                                   #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒パブリック変数
    
    def __repr__(self):                                                    #インスタンスオブジェクトを文字列化する特殊メソッドを定義
        return self.name                                                   #インスタンス変数nameのデータ(値)を戻り値として定義

lion = Lion("Dilbert")                                                     #Lionクラスを使用してインスタンスオブジェクトを作成して文字列化して変数lionに保存
print(lion)                                                                #インスタンスオブジェクトlionをと通して__repr__特殊メソッドを呼び出す⇒インスタンス変数nameが出力値(戻り値)として定義されて出力される

# objectクラスの__add__特殊メソッドをオーバーライドした場合
class AlwaysPositive():                                                    #AlwayasPositiveクラスを定義⇒objectクラスを継承している
    def __init__(self, number):                                            #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.n = number                                                    #インスタンス変数nに入力値(引数)numberのデータ(値)を保存⇒パブリック変数
    
    def __add__(self, other):                                              #インスタンスオブジェクトを加算演算子の被演算子として扱う為に__add__特殊メソッドをオーバーライド
        return abs(self.n + other.n)                                       #計算結果を出力値(戻り値)として定義

x = AlwaysPositive(-20)                                                    #AlwaysPositiveクラスを使用してインスタンスオブジェクトを作成して変数xに保存
y = AlwaysPositive(10)                                                     #AlwaysPositiveクラスを使用してインスタンスオブジェクトを作成して変数yに保存

print(x + y)                                                               #インスタンスオブジェクトxを通して__add__特殊メソッドを呼び出して入力値(引数)otherにインスタンスオブジェクトyを渡す

# <is>
# 同一のオブジェクトであることを確認
class Person():                                                            #Personクラスを定義⇒objectクラスを継承している
    def __init__(self):                                                    #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.name = "Bob"                                                  #インスタンス変数nameに文字列型オブジェクトを保存⇒パブリック変数

bob = Person()                                                             #Personクラスを使用してインスタンスオブジェクトを作成して変数bobに保存
same_bob = bob                                                             #インスタンスオブジェクトbobを変数same_bobに保存
print(bob is same_bob)                                                     #isキーワードを使用してインスタンスオブジェクトbobと変数same_bobが同一かを確認する

another_bob = Person()                                                     #Personクラスを使用してインスタンスオブジェクトを作成して変数another_bobに保存
print(bob is another_bob)                                                  #インスタンスオブジェクトbobとanother_bobが同一かを確認する⇒同じPersonクラスから作成したインスタンスオブジェクトでも作成毎に異なるインスタンスオブジェクトとして認識される

# 変数のデータ(値)がNone型オブジェクトであることを確認
x = 10                                                                     #変数xに整数型オブジェクト10を保存

if x is None:                                                              #if条件式がTrue評価の場合はコードブロックを実行
    print("x is none!!")
else:                                                                      #if条件式がFlase評価の場合
    print("x is not None!!")

x = None                                                                   #変数xにNone型オブジェクトを保存

if x is None:                                                              #if条件式がTrue評価の場合はコードブロックを実行
    print("x is None!!")
else:                                                                      #if条件式がFlase評価の場合
    print("x is not None!!")


# <チャレンジ>
# 問題1
class Square():                                                            #Squareクラスを定義⇒objectクラスを継承している
    square_list = []                                                       #クラス変数square_listに空のリスト型オブジェクトを保存

    def __init__(self, height, width):                                     #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.height = height                                               #インスタンス変数heightに入力値(引数)heightのデータ(値)を保存
        self.width = width                                                 #インスタンス変数widthに入力値(引数)widthのデータ(値)を保存
        self.square_list.append(self.height * self.width)                  #appendメソッドを使用してインスタンス変数の積をリスト型オブジェクトsquare_listに追加

square1 = Square(5, 5)                                                     #Squareクラスを使用してインスタンスオブジェクトを作成して変数square1に保存
square2 = Square(10, 10)                                                   #Squareクラスを使用してインスタンスオブジェクトを作成して変数square2に保存
square3 = Square(50, 50)                                                   #Squareクラスを使用してインスタンスオブジェクトを作成して変数square3に保存

Square.square_list                                                         #Suqareクラスを通してクラス変数square_listを取得

# 問題2
class Square():                                                            #Squareクラスを定義⇒objectクラスを継承している
    def __init__(self, length):                                            #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.len = length                                                  #インスタンス変数lenに入力値(引数)lenghtのデータ(値)を保存⇒パブリック変数
    
    def __repr__(self):                                                    #インスタンスオブジェクトを文字列化する為に__repr__特殊メソッドをオーバーライド
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

square1 = Square(4)                                                        #Squareクラスを使用してインスタンスオブジェクトを作成して変数square1に保存
square2 = Square(8)                                                        #Squareクラスを使用してインスタンスオブジェクトを作成して変数square2に保存
square3 = Square(16)                                                       #Squareクラスを使用してインスタンスオブジェクトを作成して変数square3に保存

print(square1)                                                             #インスタンスオブジェクトsquare1を出力
print(square2)                                                             #インスタンスオブジェクトsquare2を出力
print(square3)                                                             #インスタンスオブジェクトsquare3を出力

# 問題3
class Person():                                                            #Personクラスを定義⇒objectクラスを継承している
    def __init__(self, name):                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.name = name                                                   #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒パブリック変数

def check_object(obj1, obj2):
    if obj1 is obj2:                                                       #if条件式がTrue評価の場合はコードブロックを実行
        return True
    else:                                                                  #if条件式がFalse評価の場合
        return False

person = Person("Bob")                                                     #Personクラスを使用してインスタンスオブジェクトを作成して変数personに保存
another_person = Person("Bob")                                             #Personクラスを使用してインスタンスオブジェクトを作成して変数another_personに保存

print(check_object(person, person))
print(check_object(person, another_person))

# <チャレンジ(解答例)>
# 問題1
class Square():                                                            #Squareクラスを定義⇒objectクラスを継承している
    square_list = []                                                       #クラス変数square_listに空のリスト型オブジェクトを保存

    def __init__(self, s1):                                                #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.s1 = s1                                                       #インスタンス変数s1に入力値(引数)s1のデータ(値)を保存
        self.square_list.append(s1)                                        #appendメソッドを使用してリスト型オブジェクトsquare_listにインスタンスオブジェクトを追加

a_square = Square(29)                                                      #Sqaureクラスを使用すてインスタンスオブジェクトを作成して変数a_squareに保存
print(Square.square_list)                                                  #Squareクラスを通してクラス変数square_listを取得

another_square = Square(93)                                                #Squareクラスを使用してインスタンスオブジェクトを作成して変数another_squareに保存
print(Square.square_list)                                                  #Squareクラスを通してクラス変数square_listを取得

# 問題2
class Square():                                                            #Squareクラスを定義⇒objectクラスを継承している
    def __init__(self, length):                                            #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.len = length                                                  #インスタンス変数lenに入力値(引数)lengthのデータ(値)を保存⇒パブリック変数
    
    def __repr__(self):                                                    #インスタンスオブジェクトを文字列化する為に__repr__特殊メソッドをオーバーライド
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

square1 = Square(10)                                                       #Squareクラスを使用してインスタンスオブジェクトを作成して変数square1に保存
square2 = Square(50)                                                       #Squareクラスを使用してインスタンスオブジェクトを作成して変数square2に保存
square3 = Square(100)                                                      #Squareクラスを使用してインスタンスオブジェクトを作成して変数square3に保存

print(square1)                                                             #インスタンスオブジェクトsquare1を文字列として出力
print(square2)                                                             #インスタンスオブジェクトsquare2を文字列として出力
print(square3)                                                             #インスタンスオブジェクトsquare3を文字列として出力

# 問題3
def compare(obj1, obj2):                                                   #関数を定義
    return obj1 is obj2                                                    #isキーワードを利用して同じオブジェクトであることを確認

print(compare("a", "b"))