# データ構造

# <スタック>
# スタック構造をプログラミング
class Stack():                                                                              #Stackクラスを定義(objectクラスを継承)
    #データの格納先を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.items = []                                                                     #インスタンス変数itemsに空のリスト型オブジェクトを保存⇒スタック構造の容器になる！
    
    #スタックに要素(オブジェクト)が格納されているか確認
    def is_empty(self):                                                                     #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return not self.items                                                               #スタックが空の場合は「True」を出力値(戻り値)として定義

    #スタックに要素(オブジェクト)を追加
    def push(self, item):                                                                   #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.append(item)                                                             #appendメソッドを使用してスタックに入力値(引数)itemのデータ(値)を追加

    #スタックから要素(オブジェクト)を削除
    def pop(self):                                                                          #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #スタック(self.items)に対してpopメソッドを使用⇒スタックから終端の要素(オブジェクト)を削除してデータ(値)を出力値(戻り値)として定義する！

    #スタックの終端の要素(オブジェクト)を取得
    def peek(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items[-1]                                                               #スタックに対してマイナスインデックス「-1」を指定⇒最後の要素(オブジェクト)を取得して出力値(戻り値)として定義する！

    #スタックの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #スタック(self.items)の要素数を取得して出力値(戻り値)として定義

stack = Stack()                                                                             #Stackクラスを使用してインスタンスオブジェクトを作成して変数stackに保存
print(stack.is_empty())                                                                     #インスタンスオブジェクトstackを通してis_eemptyメソッドを呼び出す
stack.push(1)                                                                               #インスタンスオブジェクトstackを通してpushメソッドを呼び出す⇒入力値(引数)がスタックに追加される！
print(stack.is_empty())
item =stack.pop()                                                                           #インスタンスオブジェクトstackと通してpopメソッドを呼び出す⇒スタックの終端の要素(オブジェクト)を削除して、そのデータ(値)を取得する！
print(item)
print(stack.is_empty())

for i in range(0, 6):                                                                       #整数型オブジェクト「0-5」を変数iにイテラブルなオブジェクトとして１つずつ割り当てる
    stack.push(i)                                                                           #インスタンスオブジェクトstackを通してpushメソッドを呼び出す⇒整数型オブジェクト「0-5」が１つずつスタックに追加される！
print(stack.items)
print(stack.peek())                                                                         #インスタンスオブジェクトstackを通してpeekメソッドを呼び出す⇒スタックの終端の要素(オブジェクト)を取得して出力値(戻り値)として定義する！
print(stack.size())                                                                         #インスタンスオブジェクトstackを通してsizeメソッドを呼び出す⇒スタックの要素(オブジェクト)数を取得して出力値(戻り値)として定義する！

# <スタックを使って文字列を逆順にする>
class Stack():                                                                              #Stackクラスを定義(objectクラスを継承)
    #スタックの容器を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為に特殊メソッドをオーバーライド
        self.items = []                                                                     #インスタンス変数itemsに空のリスト型オブジェクトを保存⇒スタックの容器を作成する！
    
    #スタックに要素(オブジェクト)が格納されているか確認
    def is_empty(self):                                                                     #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return not self.items                                                               #リスト型オブジェクト(self.items)に要素(オブジェクト)が格納されているか評価判定⇒空の場合はFalse評価をnot演算子で逆転させてTrueを出力値(戻り値)として定義する！
    
    #スタックに要素(オブジェクト)を追加
    def push(self, item):                                                                   #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.append(item)                                                             #スタック(self.items)に対してappendメソッドを使用⇒入力値(引数)として受け取ったitemのデータ(値)をスタックに追加する！
    
    #スタックから要素(オブジェクト)を削除
    def pop(self):                                                                          #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #スタック(self.items)に対してpopメソッドを使用⇒スタックから最後の要素(オブジェクト)を削除して、そのデータ(値)を取得して出力値(戻り値)として定義する！
    
    #スタックの終端の要素(オブジェクト)を取得
    def peek(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items[-1]                                                               #スタック(self.items)に対してマイナスインデックス「-1」を指定⇒スタックからインデックス値に該当する要素(オブジェクト)を取得して出力値(戻り値)として定義する！
    
    #スタックの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #len関数の入力値(引数)にスタック(self.items)を渡す⇒スタックの要素(オブジェクト)数を取得して出力値(戻り値)として定義する

stack = Stack()                                                                             #Stackクラスを使用してインスタンスオブジェクトを作成して変数stackに保存
for i in "Hello":                                                                           #文字列型オブジェクトHelloをイテラブルなオブジェクトとして変数iに１つずつ割り当てる
    stack.push(i)                                                                           #インスタンスオブジェクトstackを通してpushメソッドを呼び出す⇒Helloが１文字ずつスタックに格納される！

reverse = ""                                                                                #変数reverseに空の文字列型オブジェクトを保存⇒逆順の文字列を保存する容器を作成する！

while stack.size():                                                                         #スタックの要素(オブジェクト)数が１個以上の場合(=True評価)の場合はWhileループ処理を継続、要素(オブジェクト)数がゼロ(=False評価)になるとWhileループ処理を終了
    reverse += stack.pop()                                                                  #インスタンスオブジェクトstackを通してpopメソッドを呼び出して出力値(戻り値)を変数reverseにインクリメント⇒スタックの要素(オブジェクト)を終端から取得する！
print(reverse)

# <キュー>
# キュー構造をプログラミング
class Queue():                                                                              #Queueクラスを定義(objectクラスを継承)
    #キューの容器を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.items = []                                                                     #インスタンス変数itemsに空のリスト型オブジェクトを保存⇒キュー構造の容器として使用する！
    
    #キューに要素(オブジェクト)が格納されているか確認
    def is_empty(self):                                                                     #プライメードメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return not self.items                                                               #キュー(self.items)が空の場合はTrueを出力値(戻り値)として定義⇒not演算子によりFlase評価を打ち消してTrue評価に変える！
    
    #キューに要素(オブジェクト)を追加
    def enqueue(self, item):                                                                #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.insert(0, item)                                                          #キュー(self.items)に対してinsertメソッドを使用⇒インデックス「0」の位置に入力値(引数)itemのデータ(値)を挿入する = 新しい要素(オブジェクト)は常に先頭に挿入される！
    
    #キューから要素(オブジェクト)を削除
    def dequeue(self):                                                                      #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #キュー(self.items)に対してpopメソッドを使用⇒キューの終端の要素(オブジェクト)=一番古い要素(オブジェクト)を削除して、そのデータを出力値(戻り値)として定義する！
    
    #キューの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #len関数を使用してキューの要素(オブジェクト)数を取得して出力値(戻り値)として定義

a_queue = Queue()                                                                           #Queueクラスを使用してインスタンスオブジェクトを作成して変数a_queueに保存
""""
print(a_queue.is_empty())                                                                   #インスタンスオブジェクトa_queueを通してis_emptyメソッドを呼び出す

for i in range(5):                                                                          #整数型オブジェクト0-4をイテラブルなオブジェクトとして変数iに１つずつ割り当てる
    a_queue.enqueue(i)                                                                      #インスタンスオブジェクトa_queueを通してenqueueメソッドを呼び出す⇒変数iのデータ(値)を１つずつキューの先頭から挿入する！
print(a_queue.items)
print(a_queue.size())                                                                       #インスタンスオブジェクトa_queueを通してsizeメソッドを呼び出す
"""
for i in range(5):                                                                          #整数型オブジェクト0-4をイテラブルなオブジェクトとして１つずつ変数iに割り当てる
    a_queue.enqueue(i)                                                                      #インスタンスオブジェクトa_queueを通してenqueuメソッドを呼び出す⇒変数iのデータ(値)を１つずつキューの先頭から挿入する

while a_queue.size():                                                                       #キューの要素(オブジェクト)数が１個以上=True評価の場合はwhileループ処理を継続⇒キューの要素(オブジェクト)数がゼロになるとFlase評価となりwhileループ終了！
    print(a_queue.dequeue())                                                                #インスタンスオブジェクトa_queueを通してdequeueメソッドを呼び出す⇒キューの終端の要素(オブジェクト) = 一番古い要素(オブジェクト)が削除して、そのデータ(値)を出力値(戻り値)として定義する

print(a_queue.size())

# <チケット行列>
import time
import random                                                                               #ランダムモジュールをインポート

#キューの機能を持つクラス
class Queue():                                                                              #Queueクラスを定義(objectクラスを継承)
    #キューの容器を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為に特殊メソッドをオーバーライド
        self.items = []                                                                     #インスタンス変数itemsに空のリスト型オブジェクトを保存⇒キューの容器として使用する！
    
    #キューに要素(オブジェクト)が入っているかを確認
    def is_empty(self):                                                                     #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return not self.items                                                               #キューに要素(オブジェクト)が格納されていない場合はTrue評価を出力値(戻り値)として定義⇒not演算子で評価結果を反転させる！
    
    #キューに要素(オブジェクト)を追加
    def enqueue(self, item):                                                                #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.insert(0, item)                                                          #キュー(self.items)に対してinsertメソッドを使用⇒インデックス「0」の位置に入力値(引数)itemを挿入する=新しい要素(オブジェクト)は常にキューの先頭に挿入される！
    
    #キューから要素(オブジェクト)を削除
    def dequeue(self):                                                                      #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #キュー(self.items)に対してpopメソッドを使用⇒キューの終端の要素(オブジェクト)=最初に追加した要素を削除して、そのデータ(値)を出力値(戻り値)として定義する！
    
    #キューの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #len関数を使用してキュー(self.items)の要素(オブジェクト)数を取得して出力値(戻り値)として定義
""""
queue = Queue()                                                                             #Queueクラスを使用してインスタンスオブジェクトを作成して変数queueに保存⇒キューの容器を作成する！
for i in range(5):                                                                          #整数型オブジェクト0-4をイテラブルなオブジェクトとして１つずつ変数iに割り当てる
    queue.enqueue(i)                                                                        #インスタンスオブジェクトqueueを通してenqueueメソッドを呼び出す⇒変数iに割り当てられた要素(オブジェクト)を１つずつキューに挿入する！
print(queue.items)

while queue.size():                                                                         #インスタンスオブジェクトqueueを通してsizeメソッドを呼び出す⇒キューの要素(オブジェクト)数がゼロになるとwhile条件式がFalse評価となりループ処理が終了する！
    print(queue.dequeue())                                                                  #インスタンスオブジェクトqueueを通してdequeueメソッドを呼び出す⇒キューの終端の要素(オブジェクト)=最初に追加した要素を削除して、そのデータ(値)を出力値(戻り値)として定義する！
print("the number of this queue is {}. ".format(queue.size()))
"""
#チケット行列
def simulate_line(till_show, max_time):                                                     #simulate_line関数を定義⇒入力値(引数)till_showは映画が始まるまでの時間、max_timeはチケットを購入するに必要な時間
    pq = Queue()                                                                            #Queueクラスを使用してインスタンスオブジェクトを作成して変数pqに保存⇒チケット行列に並ぶ人を保存する！
    tix_sold = []                                                                           #変数tix_soldに空のリスト型オブジェクトを保存⇒チケットを購入した人を保存する！

    #行列を作成
    for i in range(100):                                                                    #整数型オブジェクト0-99をイテラブルなオブジェクトとして１個ずつ変数iに保存
        pq.enqueue("person" + str(i))                                                       #インスタンスオブジェクトpqを通してenqueueメソッドを呼び出す⇒文字列型オブジェクトpersonと文字列に変換した変数iのデータ(値)を連結してキューに追加する！
    
    t_end = time.time() + till_show                                                         #epochからの経過時間と入力値(引数)till_showのデータ(値)を連結して変数t_endに保存
    now = time.time()                                                                       #timeモジュールを通してtimeメソッドを呼び出す⇒epochからの経過時間(=現在時刻)と変数nowに保存する！

    while now < t_end and not pq.is_empty():                                                #現在時間(now)が変数t_endより小さい間かつキューに要素(オブジェクト)が格納されている間はwhileループを継続
        now  = time.time()                                                                  #timeモジュールを通してtime関数を呼び出す⇒現在時刻(epoch)を変数nowに再保存する！
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
        return tix_sold

sold = simulate_line(1, 5)
print(sold)

# <チャレンジ>
#問題１
class Stack():                                                                              #Stackクラスを定義(objectクラスを継承)
    #スタックの容器を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為に特殊メソッドをオーバーライド⇒スタックの容器を作成する！
        self.items = []                                                                     #インスタンス変数self.itemsに空のリスト型オブジェクトを保存⇒スタックの容器になる！
    
    #スタックに要素(オブジェクト)が格納されているか確認
    def is_empty(self):                                                                     #プライベートメソッドを定義(インスタンスオブジェクトと通して呼び出し可能)
        return not self.items                                                               #スタック(self.items)に要素(オブジェクト)が格納されていない場合はTrue評価を出力値(戻り値)として定義⇒not演算子を使用して評価判定を反転させる！
    
    #スタックに要素(オブジェクト)を追加
    def push(self, item):                                                                   #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.append(item)                                                             #スタック(self.items)に対してappendメソッドを使用⇒スタックの終端に要素(オブジェクト)を追加する！
    
    #スタックから要素(オブジェクト)を削除
    def pop(self):                                                                          #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #スタック(self.items)に対してpopメソッドを使用⇒スタックの終端の要素(オブジェクト)を削除して、そのデータ(値)を取得して出力値(戻り値)として定義する！
    
    #スタックの終端の要素(オブジェクト)を取得
    def peek(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items[-1]                                                               #スタック(self.items)に対してマイナスインデックス-1を指定⇒スタックの終端の要素(オブジェクト)のデータ(値)を取得して出力値(戻り値)として定義する
    
    #スタックの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #len関数を使用してスタック(self.item)の要素(オブジェクト)数を取得して出力値(戻り値)として定義

def output(string):                                                                         #入力値(引数)stringの文字列を逆順にする関数を定義
    stack = Stack()                                                                         #Stackクラスを使用してインスタンスオブジェクトを作成して変数stackに保存⇒空のスタックが完成する！

    #スタックに要素(オブジェクト)を追加
    for i in string:                                                                        #文字列型オブジェクトstringをイテラブルなオブジェクトとして１個ずつ変数iに割り当てる
        stack.push(i)                                                                       #インスタンスオブジェクトstackを通してpushメソッドを呼び出す⇒変数iのデータ(値)を１個ずつスタックに追加する！
    print(string)

    #スタックから要素(オブジェクト)を削除＝取得
    reverse = ""                                                                            #変数reverseに空の文字列型オブジェクトを保存⇒逆順の文字列を保存する！
    while not stack.is_empty():                                                             #スタックに要素(オブジェクト)が格納されている間はwhileループ処理を継続 = スタックが空(=Flase評価)になったらWhileループを終了する！
        reverse += stack.pop()                                                              #インスタンスオブジェクトstackを通してpopメソッドを呼び出す⇒スタックの終端から要素(オブジェクト)を１個ずつ削除して、そのデータ(値)を空の文字列型オブジェクトreverseに再保存する！

    #逆順の文字列を出力
    print(reverse)

output("yesterday")                                                                         #output関数を呼び出す

#問題２
class Stack():                                                                              #Stackクラスを定義(objectクラスを継承)
    #スタックの容器を作成
    def __init__(self):                                                                     #インスタンスオブジェクトを作成する為に特殊メソッドをオーバーライド⇒スタックの容器を作成する！
        self.items = []                                                                     #インスタンス変数self.itemsに空のリスト型オブジェクトを保存⇒スタックの容器をなる！
    
    #スタックに要素(オブジェクト)が格納されているか確認
    def is_empty(self):                                                                     #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return not self.items                                                               #スタック(self.items)が空の場合はTrue評価を出力値(戻り値)として定義⇒not演算子を使用して評価判定を反転する！
    
    #スタックに要素(オブジェクト)を追加
    def push(self, item):                                                                   #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        self.items.append(item)                                                             #スタック(self.items)に対してappendメソッドを使用⇒新しい要素(オブジェクト)は常にスタックの終端に追加する！
    
    #スタックから要素(オブジェクト)を削除=取得
    def pop(self):                                                                          #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items.pop()                                                             #スタック(self.items)に対してpopメソッドを使用⇒スタックの終端の要素(オブジェクト)を削除して、そのデータ(値)を出力値(戻り値)として定義する！
    
    #スタックの終端の要素(オブジェクト)を取得
    def peek(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return self.items[-1]                                                               #スタック(self.items)に対してマイナスインデックス-1を指定⇒スタックの終端の要素(オブジェクト)を参照する！
    
    #スタックの要素(オブジェクト)数を取得
    def size(self):                                                                         #プライベートメソッドを定義(インスタンスオブジェクトを通して呼び出し可能)
        return len(self.items)                                                              #len関数を使用してスタック(self.items)の要素(オブジェクト)数を取得して出力値(戻り値)として定義

def output(my_list):                                                                        #スタックの要素を逆順に出力する関数を定義
    stack = Stack()                                                                         #Stackクラスを使用してインスタンスオブジェクトを作成して変数stackに保存⇒空のスタックが完成する！

    #スタックに要素(オブジェクト)を追加
    for i in my_list:                                                                       #入力値(引数)listをイテラブルなオブジェクトとして１個ずつ変数iに割り当てる
        stack.push(i)                                                                       #インスタンスオブジェクトstackを通してpushメソッドを呼び出す⇒変数iのデータ(値)がお１個ずつスタックの終端に追加する！
    print(stack.items)                                                                      #インスタンスオブジェクトstackを通してインスタンス変数itemsを参照

    #スタックの要素(オブジェクト)を逆順に取得
    reverse_list = []
    while stack.items:                                                                      #スタックに要素(オブジェクト)が格納されている間(=True評価)はwhileループ処理を継続 = スタックが空になった場合(=False評価)はwhileループ処理を終了する！
        reverse_list.append(stack.pop())                                                    #インスタンスオブジェクトstackを通してpopメソッドを呼び出す⇒スタックの終端の要素(オブジェクト)を削除して、そのデータ(値)をappendメソッドを使用してリスト型オブジェクトreverse_listに追加する！
    print(reverse_list)                                                                     #whileループ処理が終了したらリスト型オブジェクトreverse_listを出力

my_list = [1, 2, 3, 4, 5]                                                                   #変数my_listにリスト型オブジェクトを保存
output(my_list)                                                                             #output関数を呼び出す