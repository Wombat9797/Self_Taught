# オブジェクト指向プログラミングの４大要素

# <カプセル化>
# オブジェクトによって複数の変数とメソッドをまとめる
class Rectangle:                                                            #Rectangleクラスを定義
    def __init__(self, w, l):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = w                                                      #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒データ(値)の状態を保持
        self.len = l                                                        #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒データ(値)の状態を保持
    
    def area(self):                                                         #長方形の面積を計算するメソッドを定義
        return self.width * self.len                                        #計算結果を出力値(戻り値)として定義⇒データ(値)の状態を変更したり利用したりする

rectangle = Rectangle(10, 5)                                                #Rectabgleクラスを使用してオブジェクト(インスタンス)を作成して変数rectangleに保存
print(rectangle.area())                                                     #rectangleオブジェクト(インスタンス)を使用してareaメソッドを呼び出す

# データ(値)をクラス内に隠蔽して外から見えないようにする
class Data:                                                                 #Dataクラスを定義
    def __init__(self):                                                     #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.nums = [1, 2, 3, 4, 5]                                         #インスタンス変数numsにリスト型オブジェクトを保存
    
    def change_data(self, index, n):                                        #メソッドを定義
        self.nums[index] = n                                                #入力値(引数)として受け取ったindexのデータ(値)に該当する場所に入力値(引数)nのデータ(値)を再保存

data_one = Data()                                                           #Dataクラスを使用してオブジェクト(インスタンス)を作成して変数data_oneに保存
data_one.nums[0] = 100                                                      #data_oneオブジェクト(インスタンス)を使用してインデックス0に該当する要素に「100」を再保存⇒データ(値)を直接書き換える方法
print(data_one.nums)                                                        #data_oneオブジェクト(インスタンス)を使用してインスタンス変数numsを取得

data_two = Data()                                                           #Dataクラスを使用してオブジェクト(インスタンス)を作成して変数data_twoに保存
data_two.change_data(0, 100)                                                #data_twoオブジェクト(インスタンス)を使用してchange_dataメソッドを呼び出す⇒メソッドを通してデータ(値)を書き換える
print(data_two.nums)                                                        #data_twoオブジェクト(インスタンス)そ使用してインスタンス変数numsを取得

# プライベート変数とプライベートメソッド
class PublicPrivateExample:                                                 #PublicPrivateExampleクラスを定義
    def __init__(self):                                                     #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.public = "safe"                                                #インスタンス変数publicに文字列型オブジェクトを保存⇒パブリック変数なのでクラスの外からオブジェクト(インスタンス)を通してデータ(値)の参照と操作ができる
        self._private = "unsafe"                                            #インスタンス変数_privateに文字列型オブジェクトを保存⇒プライベート変数なのでクラスの外からオブジェクト(インスタンス)を通してデータ(値)の参照と操作ができない
    
    def public_method(self):                                                #public_methodメソッドを定義⇒パブリックメソッドなのでクラスの外からオブジェクト(インスタンス)を通して呼び出すことができる
        pass

    def _private_method(self):                                              #_private_methodメソッドを定義⇒プライベートメソッドなのでクラスの外からオブジェクト(インスタンス)を通して呼び出すことができない
        pass

# <ポリモーフィズム>
# データ型に合わせて異なる動作をする
print("Hello, world")                                                       #print関数(インターフェイス)で文字列型オブジェクトに合わせて動作する
print(100)                                                                  #print関数(インターフェイス)で整数型オブジェクトに合わせて動作する
print(200.1)                                                                #print関数(インターフェイス)で浮動小数点数型オブジェクトに合わせて動作する

type("Hello, world!")                                                       #type関数(インターフェイス)で文字列型オブジェクトに合わせて動作する
type(100)                                                                   #type関数(インターフェイス)で整数型オブジェクトに合わせて動作する
type(200.1)                                                                 #type関数(インターフェイス)で浮動小数点数型オブジェクトに合わせて動作する

# ポリモーフィズムを実装しない例
"""
shapes = [tr1, sq1, cr1]                                                    #変数shapesにリスト型オブジェクトを保存

for a_shape in shapes:                                                      #変数a_shapeにイテラブルなオブジェクトshapesの要素を1個ずつ割り当てる
    if instance(a_shape, Trinangle):
        a_shape.draw_triangle()
    if insutance(a_shape, Square):
        a_shape.draw_square()
    if insutance(a_shape, Circle):
        a_shape.draw_circle()                                               #オブジェクト毎にdrawメソッドを呼び出す必要がある
"""

# ポリモーフィズムを実装した例
"""
shapes = [tr1, sq1, cr1]                                                    #変数shapesにリスト型オブジェクトを保存

for a_shape in shapes:                                                      #変数a_shapeにイテラブルなオブジェクトshapesの要素を1個ずつ割り当てる
    a_shape.draw()                                                          #異なるデータ型を持つ複数のオブジェクトに対して一つのインターフェイス(関数やメソッド)で対応できる
"""

# <継承>
# 親クラスと子クラス1
class Shape:                                                                #Shapeクラスを定義
    def __init__(self, w, l):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = w                                                      #インスタンス変数widthに入力値(引数)wのデータ(値)を保存
        self.len = l                                                        #インスタンス変数lenに入力値(引数)lのデータ(値)を保存
    
    def print_size(self):                                                   #パブリックメソッドを定義
        print("{} by {}".format(self.width, self.len))                      #formatメソッドを使用して書式化文字列をインスタンス変数に置き換える

my_shape = Shape(20, 25)                                                    #Shapeクラスを使用してオブジェクト(インスタンス)を作成して変数my_shapeに保存
my_shape.print_size()                                                       #my_shapeオブジェクト(インスタンス)を通してprint_sizeメソッドを呼び出す

# 親クラスと子クラス2
"Parent Class"
class Shape:                                                                #Shapeクラスを定義
    def __init__(self, w, l):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = w                                                      #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒パブリック変数
        self.len = l                                                        #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒パブリック変数
    
    def print_size(self):                                                   #パブリックメソッドを定義
        print("{} by {}".format(self.width, self.len))                      #formatメソッドを使用して書式化文字列をインスタンス変数に置き換える

"Child Class"
class Square(Shape):                                                        #Shapeクラスを継承したSquareクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを使用できる
    pass

my_square = Square(20, 20)                                                  #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数my_squareに保存
my_square.print_size()                                                      #my_squareオブジェクト(インスタンス)と通してprint_sizeメソッドを呼び出す

# 子クラスにインスタンス変数やメソッドを定義
"Parent Class"
class Shape:                                                                #shapeクラスを定義
    def __init__(self, w, l):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = w                                                      #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒パブリック変数
        self.len = l                                                        #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒パブリック変数
    
    def print_size(self):                                                   #パブリックメソッドを定義
        print("{} multiply {}".format(self.width, self.len))                #formatメソッドを使用して書式化文字列をインスタンス変数に置き換える

"Child Class"
class Square(Shape):                                                        #Shapeクラスを継承したSquareクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを使用できる
    def area(self):                                                         #パブリックメソッドを定義
        return self.width * self.len                                        #インスタンス変数widthとlenの積を出力値(戻り値)として定義

a_square = Square(20, 20)                                                   #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数a_squareに保存
a_square.print_size()                                                       #a_squareオブジェクト(インスタンス)を通してprint_sizeメソッドを呼び出す
print(a_square.area())                                                      #a_squareオブジェクト(インスタンス)を通してareaメソッドを呼び出す

# メソッドオーバーライド
"Parent Class"
class Shape:                                                                #Shapeクラスを定義
    def __init__(self, w, l):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = w                                                      #インスタンス変数widthに入力値(引数)wのデータ(値)を保存⇒パブリック変数
        self.len = l                                                        #インスタンス変数lenに入力値(引数)lのデータ(値)を保存⇒パブリック変数
    
    def print_size(self):                                                   #パブリックメソッドを定義
        print("{} by {}".format(self.width, self.len))                      #formatメソッドを使用して書式化文字列をインスタンス変数に置き換える

"Child Class"
class Square(Shape):                                                        #Shapeクラスを継承したSquareクラスを定義⇒Shapeクラスのインスタンス変数をメソッドを使用できる
    def area(self):                                                         #パブリックメソッドを定義
        return self.width * self.len                                        #インスタンス変数widthとlenの積を出力値(戻り値)として定義
    
    def print_size(self):                                                   #Shapeクラスのメソッドをオーバーライド
        print("I am {} by {}.".format(self.width, self.len))                #formatメソッドを使用して書式化文字列をインスタンス変数に置き換える

a_square = Square(20, 25)                                                   #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数a_squareに保存
print(a_square.area())                                                      #a_squareオブジェクト(インスタンス)を通してareaメソッドを呼び出す
a_square.print_size()                                                       #a_squareオブジェクト(インスタンス)を通してオーバーライドしたprint_sizeメソッドを呼び出す

a_shape = Shape(20, 25)                                                     #Shapeクラスを使用してオブジェクト(インスタンス)を作成して変数a_shapeに保存
a_shape.print_size()                                                        #a_shapeオブジェクト(インスタンス)を通してprint_sizeメソッドを呼び出す⇒Squareクラスは干渉しないのでオーバーライドされる前の処理が実行される


# <コンポジション>
class Dog:                                                                  #Dogクラスを定義
    def __init__(self, name, breed, owner):                                 #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.name = name                                                    #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒パブリック変数
        self.breed = breed                                                  #インスタンス変数breedに入力値(引数)breedのデータ(値)を保存⇒パブリック変数
        self.owner = owner                                                  #インスタンス変数ownerに入力値(引数)ownerのデータ(値)を保存⇒パブリック変数

class Person:                                                               #Personクラスを定義
    def __init__(self, name):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.name = name                                                    #インスタンス変数nameに入力値(引数)nameの入力値(引数)を保存⇒パブリック変数

mick = Person("Mick Jagger")                                                #Personクラスを使用してオブジェクト(インスタンス)を作成して変数mickに保存
stan = Dog("Stanley", "Bulldog", mick)                                      #Dogクラスを使用してオブジェクト(インスタンス)を作成して変数stanに保存⇒ownerに渡す入力値(引数)にmickオブジェクトを使用する
print(stan.owner.name)                                                      #stanオブジェクトを通してインスタンス変数ownerに保存されているPersonクラスのインスタンス変数nameを取得

# <チャレンジ>
# 問題1
class Rectangle:                                                            #Rectangleクラスを定義
    def __init__ (self, vertical, horizon):                                 #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.vertical = vertical                                            #インスタンス変数verticalに入力値(引数)verticalのデータ(値)を保存⇒パブリック変数
        self.horizon = horizon                                              #インスタンス変数horizonに入力値(引数)horizonのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #長方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return (self.vertical + self.horizon) / 2                           #計算結果を出力値(戻り値)として定義

class Square:                                                               #Squareクラスを定義
    def __init__(self, len):                                                #オブジェクト(インスタンス)を作成する為に特殊メソッドを定義
        self.len = len                                                      #インスタンス変数lenに入力値(引数)lenのデータ(値)を保存⇒パブリック変数

    def calculate_perimeter(self):                                          #正方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.len * 4                                                 #計算結果を出力値(戻り値)として定義

rectangle = Rectangle(5, 10)                                                #Rectangleクラスを使用してオブジェクト(インスタンス)を作成して変数rectangleに保存
print(rectangle.calculate_perimeter())                                      #rectangleオブジェクト(インスタンス)を通してcalculate_perimeterメソッドを呼び出す

square = Square(10)                                                         #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数squareに保存
print(square.calculate_perimeter())                                         #squareオブジェクト(インスタンス)と通してcalculate_perimeterメソッドを呼び出す

# 問題2
class Square:                                                               #Squareクラスを定義
    def __init__(self, len, change):                                        #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.len = len                                                      #インスタンス変数lenに入力値(引数)lenのデータ(値)を保存⇒パブリック変数
        self.change = change                                                #インスタンス変数changeに入力値(引数)changeのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #正方形の外周の長さを計算するメソッドを定義⇒パブリックメソッド
        return self.len * 4                                                 #計算結果を出力値(戻り値)として定義
    
    def change_size(self):                                                  #正方形の一辺の長さを変更して外周を計算するメソッドと定義⇒パブリックメソッド
        return (self.len + self.change) * 4

square = Square(10, 5)                                                      #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数squareに保存
print(square.calculate_perimeter())                                         #squareオブジェクト(インスタンス)を通してcalculate_perimeterメソッドを呼び出す
print(square.change_size())                                                 #squareオブジェクト(インスタンス)を通してchange_sizeメソッドを呼び出す

# 問題3
class Shape:                                                                #Shapeクラスを定義
    def what_am_i(self):                                                    #パブリックメソッドを定義
        print("I am a shape!")

class Rectangle(Shape):                                                     #Shapeクラスを継承したRectangleクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを利用できる
    def __init__(self, vertical, horizon):                                  #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.vertical = vertical                                            #インスタンス変数verticalに入力値(引数)verticalのデータ(値)を保存⇒パブリック変数
        self.horizon = horizon                                              #インスタンス変数horizonに入力値(引数)horizonのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #長方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return (self.vertical + self.horizon) / 2                           #計算結果を出力値(戻り値)として定義

class Square(Shape):                                                        #Shapeクラスを継承したSquareクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを利用できる
    def __init__(self, len):                                                #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.len = len                                                      #インスタンス変数lenに入力値(引数)lenのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #正方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.len * 4                                                 #計算結果を出力値(戻り値)として定義

rectangle = Rectangle(5, 10)                                                #Rectangleクラスを使用してオブジェクト(インスタンス)を作成して変数rectangleに保存
rectangle.what_am_i()                                                       #rectangleオブジェクト(インスタンス)を通してwhat_am_iメソッドを呼び出す

square = Square(5)                                                          #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数squareに保存
square.what_am_i()                                                          #squareオブジェクト(インスタンス)と通してwhat_am_iメソッドを呼び出す

# 問題4
class Hose:                                                                 #Hoseクラスを定義
    def __init__(self, hose_name, rider_name):                              #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.hose_name = hose_name                                          #インスタンス変数hose_nameに入力値(引数)hose_nameのデータ(値)を保存⇒パブリック変数
        self.rider_name = rider_name                                        #インスタンス変数rider_nameに入力値(引数)rider_nameのデータ(値)を保存⇒パブリック変数

class Rider:                                                                #Riderクラスを定義
    def __init__(self, person):                                             #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.person = person                                                #インスタンス変数personに入力値(引数)personのデータ(値)を保存⇒パブリック変数

rider = Rider("Jack Miner")                                                 #Riderクラスを使用してオブジェクト(インスタンス)を作成して変数riderに保存
hose = Hose("Stanley", rider)                                               #Hoseクラスを使用してオブジェクト(インスタンス)を作成して変数hoseに保存⇒入力値(引数)にRiderクラスを使用して作成したriderオブジェクト(インスタンス)を渡す
hose.rider_name.person                                                      #hoseオブジェクト(インスタンス)を通してインスタンス変数rider_nameに保存されたインスタンス変数personの値を取得

# <チャレンジ(解答例)>
# 問題1
class Rectangle():                                                          #Rectangleクラスを定義
    def __init__(self, width, length):                                      #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = width                                                  #インスタンス変数widthに入力値(引数)widthのデータ(値)を保存⇒パブリック変数
        self.length = length                                                #インスタンス変数lengthに入力値(引数)lengthのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #長方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.width * 2 + self.length * 2                             #計算結果を出力値(戻り値)として定義

class Square():                                                             #Squareクラスを定義
    def __init__(self, s1):                                                 #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.s1 = s1                                                        #インスタンス変数s1に入力値(引数)s1のデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #正方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.s1 * 4                                                  #計算結果を出力値(戻り値)として定義


a_rectangle = Rectangle(25, 50)                                             #Rectangleクラスを使用してオブジェクト(インスタンス)を作成して変数a_rectangleに保存
a_square = Square(20)                                                       #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数a_squareに保存

print(a_rectangle.calculate_perimeter())                                    #a_rectangleオブジェクト(インスタンス)を通してcalculate_perimeterメソッドを呼び出す
print(a_square.calculate_perimeter())                                       #a_squareオブジェクト(インスタンス)と通してcalculate_perimeterメソッドを呼び出す

# 問題2
class Square():                                                             #Squareクラスを定義
    def __init__(self, s1):                                                 #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.s1 = s1                                                        #インスタンス変数s1に入力値(引数)s1のデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #正方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.s1 * 4                                                  #計算結果を出力値(戻り値)として定義
    
    def change_size(self, new_size):                                        #正方形の１辺の長さを変更するメソッドを定義⇒パブリックメソッド
        self.s1 += new_size                                                 #インスタンス変数s1に入力値(引数)new_sizeのデータ(値)を加算して再保存

a_square = Square(100)                                                      #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数a_squareに保存
print(a_square.s1)                                                          #a_squareオブジェクト(インスタンス)と通してインスタンス変数s1のデータ(値)を取得

a_square.change_size(200)                                                   #a_squareオブジェクト(インスタンス)と通してchange_sizeメソッドを呼び出す
print(a_square.s1)                                                          #a_squareオブジェクト(インスタンス)を通してインスタンス変数s1のデータ(値)を取得

# 問題3
"Parent Class"
class Shape():                                                              #Shapeクラスを定義
    def what_am_i(self):                                                    #パブリックメソッドを定義
        print("I am a shape!")

"Child Class"
class Rectangle(Shape):                                                     #Shapeクラスを継承したRectangleクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを使用できる
    def __init__(self, width, length):                                      #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.width = width                                                  #インスタンス変数widthに入力値(引数)widthのデータ(値)を保存⇒パブリック変数
        self.length = length                                                #インスタンス変数lengthに入力値(引数)lengthのデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #長方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.width * 2 + self.length * 2                             #計算結果を出力値(戻り値)として定義

"Child Class"
class Square(Shape):                                                        #Shapeクラスを継承したSquareクラスを定義⇒Shapeクラスのインスタンス変数とメソッドを使用できる
    def __init__(self, s1):                                                 #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.s1 = s1                                                        #インスタンス変数s1に入力値(引数)s1のデータ(値)を保存⇒パブリック変数
    
    def calculate_perimeter(self):                                          #正方形の外周を計算するメソッドを定義⇒パブリックメソッド
        return self.s1 * 4                                                  #計算結果を出力値(戻り値)として定義

a_rectangle = Rectangle(20, 50)                                             #Rectangleクラスを使用してオブジェクト(インスタンス)を作成して変数a_rectangleに保存
a_square = Square(29)                                                       #Squareクラスを使用してオブジェクト(インスタンス)を作成して変数a_squareに保存

a_rectangle.what_am_i()                                                     #a_rectangleオブジェクト(インスタンス)と通してwhat_am_iメソッドを呼び出す
a_square.what_am_i()                                                        #a_squareオブジェクト(インスタンス)を通してwhat_am_iメソッドを呼び出す

# 問題4
class Rider():                                                              #Riderクラスを定義
    def __init__(self, name):                                               #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.name = name                                                    #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存

class Hose():                                                               #Hoseクラスを定義
    def __init__(self, name, rider):                                        #オブジェクト(インスタンス)を作成する為の特殊メソッドを定義
        self.name = name                                                    #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒パブリック変数
        self.rider = rider                                                  #インスタンス変数riderに入力値(引数)riderのデータ(値)を保存⇒パブリック変数

the_rider = Rider("Sally")                                                  #Riderクラスを使用してオブジェクト(インスタンス)を作成して変数the_riderに保存
harry_the_hose = Hose("Harry", the_rider)                                   #Hoseクラスを使用してオブジェクト(クラス)を作成して変数harry_the_hoseに保存⇒the_riderオブジェクト(インスタンス)を入力値(引数)として渡す

print("The name of hose is {}.".format(harry_the_hose.name))                #formatメソッドを使用して書式化文字列をharry_the_hoseオブジェクト(インスタンス)のインスタンス変数に置き換える
print("The name of rider is {}.".format(harry_the_hose.rider.name))         #formatメソッドを使用して書式化文字列をharry_the_hoseオブジェクト(インスタンス)のインスタンス変数riderに保存されているRiderクラスのインスタンス変数nameに置き換える