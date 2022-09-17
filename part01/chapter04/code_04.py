# 関数

# <関数>
# 関数の定義
def f(x):        #関数名と引数を定義
    return x * 2 #実行する処理と関数が呼び出された時の出力値(戻り値)を定義

# 関数を呼び出す
def f(x):
    return x * 4 #「2 * 4」の結果である「8」が出力値(戻り値)として定義される

f(2)             #関数fを呼び出して入力値(引数)に「2」を渡す

# 関数の出力値(戻り値)を変数に保存
def f(x):
    return x * 4

result = f(2)    #変数resultに関数fの出力値(戻り値)を保存
print(result)

# 関数の出力値(戻り値)を変数に保存して別の場所で使用
def f(x):
    return x + 1

z = f(4)                 #変数zに関数fの出力値(戻り値)を保存
if z == 5:               #関数fの出力値(戻り値)をif-else文で使用する
    print("z is 5.")
else:
    print("z is not 5.")

# 引数を必要としない関数
def f():               #引数を定義しない＝入力値を必要としない
    return 1 + 1

result = f()           #変数resultに関数fの出力値(戻り値)を保存
print(result)

# 複数の引数を持つ関数
def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)  #関数fを呼び出して複数の引数を渡す
print(result)

# returnが無い関数
def h():
    x = 1 + 1 #出力値(戻り値)を定義しない＝関数を呼び出してもNoneType型オブジェクトしか返ってこない

z = h()
print(z)

# <組み込み関数>
# len関数
len("Monty") #文字列型オブジェクトMontyの長さを出力する
len("Python") #文字列型オブジェクトPythonの長さを出力する

# str関数
str(100)  #整数型オブジェクト100を文字列型オブジェクトに変換する

# int関数
int("1")   #文字列型オブジェクト1を整数型オブジェクトに変換する
int("100") #文字列型オブジェクト100を整数型オブジェクトに変換する
int(20.54) #浮動小数点数型オブジェクト20.54を整数型オブジェクトに変換する

# float関数
float(100)    #整数型オブジェクト100を浮動小数点数型オブジェクトに変換する
float("16.4") #文字列型オブジェクト16.4を浮動小数点数型オブジェクトに変換する
float(99)     #整数型オブジェクト99を浮動小数点数型オブジェクトに変換する

# 整数または浮動小数点数に変換できない入力値(引数)
int("Prince")
float("King")

# input関数
age = input("Enter your age: ") #変数ageにinput関数の文字列型オブジェクト出力値を保存
int_age = int(age)              #変数int_ageに文字列型オブジェクトageを整数型オブジェクトに変換して保存

if int_age < 21:                #inpput関数の出力値をif-else文の条件式として使用する
    print("You ara young!")
else:
    print("Wow, your are old!")

# <関数を再利用する>
# 関数を使用しない例
n = input("type a number: ") #変数nにinput関数の文字列型オブジェクトの出力値を保存
n = int(n)                 #変数nに文字列型オブジェクトnを整数型オブジェクトに変換して再保存
if n % 2 == 0:             #変数nに保存されたinput関数の出力値をif-else文の条件式に使用する
    print("n is even!")
else:
    print("n is odd!")

n = input("type a number: ")
n = int(n)
if n % 2 == 0:
    print("n is even!")
else:
    print("n is odd!")

n = input("type a number: ")
n = int(n)
if n % 2 == 0:
    print("n is even!")
else:
    print("n is odd!")

# 関数を使用した例
def even_odd():                  #関数even_oddを定義
    n = input("type a number: ") #変数nにinput関数の文字列型オブジェクトの出力値を保存
    n = int(n)                   #変数nに文字列型オブジェクトnを整数型オブジェクトに変換して再保存

    if n % 2 == 0:               #変数nに保存されたinput関数の出力値をif-else文の条件式で使用する
        print("n is even!")
    else:
        print("n is odd!")

even_odd()
even_odd()
even_odd()                       #関数even_oddを3回呼び出して値を3回入力する

# <必須引数とオプション引数>
# オプション引数を定義
def f(x=2):          #オプション引数xを定義してデフォルト値を「2」に設定する
    return x ** x

print(f())           #入力値(引数)を渡さないで関数fを呼び出す
print(f(4))          #入力値(引数)を渡して関数fを呼び出す

# 必須引数とオプション引数を定義
def add_it(x, y=10):
    return x + y

result = add_it(2)   #関数add_itを呼び出して必須引数xに「2」を渡す(オプション引数は入力値が省略されているのでデフォルト値が使用される)
print(result)

# <スコープ>
# グローバルスコープ(グローバル変数)
x = 1
y = 2
z = 3        #グローバル変数x・y・z・に整数型オブジェクトを保存

def f():
    print(x)
    print(y)
    print(z) #関数fの中からグローバル変数x・y・zを検索・参照する

f()

# ローカル変数を関数やクラスの外から検索・参照・変更した場合
def f():
    a = 1
    b = 2
    c = 3 #ローカル変数a・b・cに整数型オブジェクトを保存

#try:
    #print(a)
    #print(b)
    #print(c)  #関数fの外からローカル変数a・b・cを検索・参照する
#except NameError:
    print("a.b.c is local variable!")

# ローカル変数を関数やクラスの中で検索・参照・変更した場合
def f():
    x = 1
    y = 2
    z = 3 #ローカル変数x・y・zに整数型オブジェクトを保存

    print(x)
    print(y)
    print(z) #関数fの中でローカル変数x・y・zを検索・参照する

f()

# ローカルスコープの中からグローバルスコープ(グローバル変数)を変更
x = 100

def f():
    global x #globalキーワードを使用して対象のグローバル変数xを明示的に指定する
    x += 1   #グローバル変数xに「+1」した値を再保存
    print(x)

f()

# <例外処理>
# 例外が発生するプログラムの例
a = input("type a number: ")
b = input("type a another: ")
a = int(a)
b = int(b)
print(a / b)

# 例外処理を定義したプログラムの例
a = input("type a number: ")    #変数aにinput関数の文字列型オブジェクトの出力値を保存
b = input("type another: ")
a = int(a)                      #変数aに文字列型オブジェクトaを整数型オブジェクトに変換して再保存
b = int(b)

try:
    print(a / b)                #例外が発生する可能性を持つ処理であることを定義
except ZeroDivisionError:       #発生する可能性のある例外を定義
    print("b can not be Zero!") #例外を発生させる代わりに実行する処理を定義

# 複数の例外処理を想定したプログラムの例
a = input("type a number: ")
b = input("type another: ")

try:                                    #例外が発生する可能性を持つ処理であることを定義
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError): #発生する可能性のある例外を定義
    print("Invalid input!")             #例外を発生させる代わりに実行する処理を定義

# 例外処理の注意点
try:
    10 / 0                          #例外が発生する場所
    c = "I will never get defined!" #例外が発生した場合は定義されない
except ZeroDivisionError:
    print("c")

# <ドキュメンテーション文字列(docstring)>
# ドキュメンテーション文字列の定義
def add(x, y):
    """
    Returns x + y.              #関数の目的を説明
    :param x: int.              #関数の引数の種類とデータ型を説明
    :param y: int.
    :return: int sum of x and y #関数の出力値(戻り値)の内容を説明
    """
    return x + y

add(2, 3)

# <チャレンジ>
# 問題1
def squared(x):   #関数名と引数を定義
    return x ** 2 #実行する処理と出力値(戻り値)を定義

print(squared(3))

# 問題2
def print_string(x, y):            #関数名と引数を定義
    print(x)
    print(y)                       #実行する処理を定義(printで出力するためreturnは定義しない)

a = "Hello, everyone!"
b = "I'm learning Pyhotn"
print_string(a, b)                 #関数print_stringを呼び出して入力値(引数)に文字列型オブジェクトa・bを渡す

# 問題3
def add_mult(a, b, c, x=100, y=1000): #関数名と必須引数、オプション引数とデフォルト値を定義
    return a + b + c * x * y          #実行する処理と出力値(戻り値)を定義

print(add_mult(10, 50, 300))          #関数add_multを呼び出して必須引数に入力値(引数)を渡す

# 問題4
def divide(x):          #関数名と引数を定義
    return x / 2        #実行する処理と出力値(戻り値)を定義

def multiply(x):        #関数名と引数を定義
    return x * 4        #実行する処理と出力値(戻り値)を定義

result = divide(10)     #変数resultに関数divideの出力値(戻り値)を保存
print(multiply(result)) #関数multiplyを呼び出して入力値(引数)に関数divideの整数型オブジェクト出力値を渡す

# 問題5
def convert(string):                                      #関数名と引数を定義
    try:                                                  #例外が発生する可能性を持つ処理であることを定義
        return float(string)
    except ValueError:                                    #発生する可能性がある例外を定義
        print("Could not convert the string to a float!") #例外が発生した時に実行する代わりの処理を定義

z = input("type something: ")
print(convert(z))

# 問題6
def squared(x):
    """
    Returns Take an int and returns it multiplied by 2. #関数の目的を説明
    :param x: int.                                      #引数の種類とデータ型を説明
    :return: multiplied by 2.                           #出力値(戻り値)の内容を説明
    """
    return x ** 2

def print_string(x, y):
    """
    Returns Prints the string passed in. #関数の目的を説明
    :param x: string.                    #引数の種類とデータ型を説明
    :param y: string.
    :return: print x and y.              #出力値(戻り値)の内容を説明
    """
    print(x)
    print(y)

a = "Hello, everyone!"
b = "I'm learning Pyhotn"
print_string(a, b)

def all_sum(a, b, c, x=100, y=1000):
    """
    Returns Returns the result of two optional params 
            multiplied by the addition of three required params. #関数の目的を説明
    :param a: int.                                               #引数の種類とデータ型を説明
    :param b: int.
    :param c: int.
    :param x: int.
    :param y: int.
    :return: int.                                                #出力値(戻り値)の内容を説明
    """
    return a + b + c * x * y

print(all_sum(10, 50, 300))

def divide(x):
    """
    Returns Takes an int and returns it divided by 2. #関数の目的を説明
    :param x: int.                                    #引数の種類とデータ型を説明
    :return: int.                                     #出力値(戻り値)の内容を説明
    """
    return x / 2

def multi(y):
    """
    Returns Takes an int and returns it multiplied by 4. #関数の目的を説明
    :param y: int.                                       #引数の種類とデータ型を説明
    :return: int                                         #出力値(戻り値)の内容を説明
    """
    return y * 4

result = divide(10)
print(multi(result))

def convert(string):
    """
    Returns Convert passed in string to float. #関数の目的を説明
    :param string: str.                        #引数の種類とデータ型を説明
    :return: string converted to float.        #出力値(戻り値)の内容を説明
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float!")

z = input("type something: ")
print(convert(z))