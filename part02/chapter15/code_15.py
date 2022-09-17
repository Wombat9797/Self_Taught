# 知識を１つにまとめる

# <War(戦争)>
from ast import Return
from random import shuffle
from tkinter import W
from unicodedata import name                                                           #randomモジュールからshuffleメソッドをインポート⇒カードデッキを作成する時に使用

# カード
class Card():                                                                        #Cardクラスを定義⇒objectクラスを継承している
    suits = ["spades", "hearts", "diamonds", "clubs"]                                #クラス変数suitsにリスト型オブジェクトを保存⇒カードのマーク(suit)を保存する
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"]                                                  #クラス変数valuesにリスト型オブジェクトを保存⇒カードの値(value)を保存する

    #カードを作成
    def __init__(self, v, s):                                                        #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒１枚カードを作成する
        self.value = v                                                               #インスタンス変数valueに入力値(引数)vのデータ(値)を保存⇒カードの値(value)を保存する
        self.suit = s                                                                #インスタンス変数suitに入力値(引数)sのデータ(値)を保存⇒カードのマーク(suit)を保存する
    
    #プレイヤーのカードの値とマークが対戦相手より弱いかを判定
    def __lt__(self, c2):                                                            #インスタンスオブジェクトを「<」演算子の被演算子として扱えるように__lt__特殊メソッドをオーバーライド
        if self.value < c2.value:                                                    #プレイヤーのカードの値(self.value)が対戦相手のカードの値(c2.value)より小さい場合
            return True                                                              #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        if self.value == c2.value:                                                   #プレイヤーのカードの値(self.value)と対戦相手のカードの値(c2.value)が等価の場合⇒False評価の場合は次のコードを実行する
            if self.suit < c2.suit:                                                  #プレイヤーのカードのマーク(self.suit)が対戦相手のマーク(c2.suit)より小さい場合
                return True                                                          #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義
            else:
                return False                                                         #if条件式がFalse評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義
        return False                                                                 #全てのif条件式がFalse評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義⇒プレイヤーのカードの値(value)の方が大きい
    
    #プレイヤーのカードの値とマークが対戦相手より強いかを判定
    def __gt__(self, c2):                                                            #インスタンスオブジェクトを「>」演算子の被演算子として扱えるように__gl_特殊メソッドをオーバーライド
        if self.value > c2.value:                                                    #プレイヤーのカードの値(value)が対戦相手のカードの値(c2.value)より大きい場合
            return True                                                              #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        if self.value == c2.value:                                                   #プレイヤーのカードの値(self.value)と対戦相手のカードの値(c2.value)が等価の場合⇒Flase評価の場合は次のコードを実行する
            if self.suit > c2.suit:                                                  #プレイヤーのカードのマーク(self.suit)が対戦相手のカードのマーク(c2.suit)より大きい場合
                return True                                                          #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義
            else:
                return False                                                         #if条件式がFalse評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義
        return False                                                                 #全ての条件式がFalse評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義⇒プレイヤーのカードの値(value)の方が小さい
    
    #カードの値とマークを文字列として出力
    def __repr__(self):                                                              #インスタンスオブジェクトを文字列化する為に__repr__特殊メソッドをオーバーライド
        v = Card.values[self.value] + " of " + Card.suits[self.suit]                 #Cardクラスを通してクラス変数valuesとsuitsからインスタンス変数valueとsuitのデータ(値)に該当するインデックス値の要素を取得して変数vに保存
        return v                                                                     #変数vのデータ(値)を出力値(戻り値)として定義

# デッキ
class Deck():                                                                        #Deckクラスを定義⇒objectクラスを継承している
    #５２枚の山札を作成
    def __init__(self):                                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.cards = []                                                              #インスタンス変数cardsに空のリスト型オブジェクトを保存⇒Cardクラスで作成したカードを１枚ずつ保存する
        for i in range(2, 15):                                                       #変数iにvaluesリストのインデックス値をイテラブルなオブジェクトとして１個ずつ割り当てる⇒カードの番号を取得
            for j in range(4):                                                       #変数jにsuitsリストのインデックス値をイテラブルなオブジェクトとして１個ずつ割り当てる⇒カードのマークを取得
                self.cards.append(Card(i, j))                                        #appendメソッドを使用してcardsリストにCardクラスで作成したカードを１枚ずつ追加⇒５２枚のカードを追加した時点で２重ループ処理は終了する
        shuffle(self.cards)                                                          #randomモジュールのshuffleメソッドを使用してカードデッキ(self.cards)をランダムに並び替える
    
    #カードデッキの枚数を判定(デッキからカードを１枚減らす)
    def rm_card(self):                                                               #パブリックメソッドを定義
        if len(self.cards) == 0:                                                     #カードデッキ(self.cards)の要素数がゼロの場合
            return                                                                   #if条件式がTrue評価の場合はNone型オブジェクトを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        return self.cards.pop()                                                      #popメソッドを使用してカードデッキ(self.cards)から最後の要素(=一番上のカード)を削除して出力値(戻り値)として定義⇒引いたカードの値とマークを取得してカードデッキからカードを１枚ずつ減らしていく

# プレイヤー
class Player():                                                                      #Playerクラスを定義⇒objectクラスを継承している
    def __init__(self, name):                                                        #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒プレイヤー情報を保存する
        self.wins = 0                                                                #インスタンス変数winsに整数型オブジェクト0を保存⇒プレイヤーが勝った回数を保存する
        self.card = None                                                             #インスタンス変数cardにNone型オブジェクトを保存⇒プレイヤーが持っているカードを保存する
        self.name = name                                                             #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒プレイヤー名を保存んする

# ゲーム自体
class Game():                                                                        #Gameクラスを定義⇒objectクラスを継承している
    # カードデッキとプレイヤー初期情報を作成
    def __init__(self):                                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒カードデッキと初期のプレイヤー情報を作成
        name1 = input("プレイヤー１の名前 ")                                           #変数name1にinput関数の文字列型オブジェクト出力値(戻り値)を保存
        name2 = input("プレイヤー２の名前 ")                                           #変数name2にinput関数の文字列型オブジェクト出力値(戻り値)を保存
        self.deck = Deck()                                                           #インスタンス変数deckにDeckクラスのインスタンスオブジェクトを保存⇒５２枚のカードデッキが完成する　※DeckクラスにはCardクラスのインスタンスオブジェクトも保存されているので、Cardクラスのインスタンス変数やメソッドを呼び出すことも可能になる
        self.p1 = Player(name1)                                                      #インスタンス変数p1にPlayerクラスのインスタンスオブジェクトを保存⇒プレイヤー１の初期情報が完成する
        self.p2 = Player(name2)                                                      #インスタンス変数p2にPlayerクラスのインスタンスオブジェクトを保存⇒プレイヤー２の初期情報が完成する

    #ラウンド毎の勝利プレイヤーを表示
    def wins(self, winner):                                                        #パブリックメソッドを定義
        w = "このラウンドは{}が勝ちました！"                                            #変数wに文字列型オブジェクトを保存
        w = w.format(winner)                                                         #formatメソッドを使用して書式化文字列を入力値(引数)winnerに置き換えて変数wに再保存
        print(w)
    
    #プレイヤーのカードを表示
    def draw(self, p1n, p1c, p2n, p2c):                                              #パブリックメソッドを定義
        d = "{}は{}、{}は{}を引きました！"                                             #変数dに文字列型オブジェクトを保存⇒プレイヤーが引いたカードを表示する
        d = d.format(p1n, p1c, p2n, p2c)                                             #formatメソッドを使用して書式化文字列を入力値(引数)p1n-p2cに置き換えて変数dに再保存
        print(d)
    
    #ゲーム実行
    def play_game(self):                                                             #パブリックメソッドを定義
        cards = self.deck.cards                                                      #インスタンスオブジェクトdeckを通してインスタンス変数cardsのデータ(値)を取得して変数cardsに保存⇒５２枚のカードデッキを用意できた
        print("戦争を始めます！")
        while len(cards) >= 2:                                                       #Cardsリストの要素数が２未満になるまでループ処理を継続
            #ゲームの開始終了
            m = "qで終了、それ以外のキーでPlay:"                                       #変数mに文字列型オブジェクトを保存
            response = input(m)                                                      #変数responseにinput関数の文字列型オブジェクト出力値を保存
            if response == "q":                                                      #変数responseのデータ(値)が文字列型オブジェクト「q」と等価の場合
                break                                                                #if条件式がTrue評価の場合はbreakキーワードを使用してループ処理を終了⇒false評価の場合は次のコードを実行する

            #プライヤーが引いたカードを表示
            p1c = self.deck.rm_card()                                                #インスタンスオブジェクトdeckを通してrm_cardメソッドを呼び出す⇒プレイヤー１が引いたカードの値とマークを取得して、デッキからカードを１枚減らす
            p2c = self.deck.rm_card()                                                #インスタンスオブジェクトdeckを通してrm_cardメソッドを呼び出す⇒プライヤー２が引いたカードの値とマークを取得して、デッキからカードを１枚減らす
            p1n = self.p1.name                                                       #インスタンスオブジェクトp1を通してインスタンス変数nameのデータ(値)を取得⇒プレイヤー１の名前を取得する
            p2n = self.p2.name                                                       #インスタンスオブジェクトp2を通してインスタンス変数nameのデータ(値)を取得⇒プレイヤー２の名前を取得する
            self.draw(p1n, p1c, p2n, p2c)                                            #drawメソッドを呼び出してプレイヤーの名前とカードを出力

            #ラウンドの勝ち負けを判定
            if p1c > p2c:                                                            #「>」演算子を通してCardクラスの__gt__特殊メソッドをオーバーライド⇒p1c.__gt__(p2c)
                self.p1.wins += 1                                                    #if条件式がTrue評価の場合はインスタンスオブジェクトp1を通してインスタンス変数winsをインクリメントして再保存
                self.wins(self.p1.name)                                              #winsメソッドを呼び出す⇒プレイヤー１の名前を表示する
            else:
                self.p2.wins += 1                                                    #if条件式がFalse評価の場合はインスタンスオブジェクトp2を通してインスタンス変数winsをインクリメントして再保存
                self.wins(self.p2.name)                                              #winsメソッドを呼び出す⇒プレイヤー２の名前を表示する

        #ゲームの勝ち負けを判定
        win = self.winner(self.p1, self.p2)                                          #winnerメソッドを出力値(戻り値)を変数winに保存⇒コンポジションを利用して入力値(引数)にインスタンスオブジェクトを渡す
        print("ゲーム終了、{}の勝利です！".format(win))                                #formatメソッドを使用して書式化文字列を変数winのデータ(値)に置き換える⇒勝利プレイヤーの名前を出力する
    
    #プレイヤーの勝利回数を判定
    def winner(self, p1, p2):                                                        #パブリックメソッドを定義
        if p1.wins > p2.wins:                                                        #インスタンスオブジェクトp1のインスタンス変数winsのデータ(値)がインスタンスオブジェクトp2のインスタンス変数winsより大きい場合
            return p1.name                                                           #if条件式がTrue評価の場合はインスタンスオブジェクトp1のインスタンス変数nameのデータ(値)を出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        if p1.wins < p2.wins:                                                        #インスタンス変数p1のインスタンス変数winsのデータ(値)がインスタンスオブジェクトp2のインスタンス変数winsより小さい場合
            return p2.name                                                           #if条件式がTrue評価の場合はインスタンスオブジェクトp2のインスタンス変数nameのデータ(値)を出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        return "引き分け！"                                                           #全ての条件式がFalse評価の場合は文字列型オブジェクト「引き分け」を出力値(戻り値)として定義

game = Game()                                                                        #Gameクラスを使用してインスタンスオブジェクトを作成して変数gameに保存⇒カードデッキとプレイヤー初期情報が作成される
game.play_game()                                                                     #インスタンスオブジェクトgameを通してplay_gameメソッドを呼び出す

# <War(戦争)>_Review
from random import shuffle                                                           #randomモジュールからshuffleメソッドをインポート

#カード
class Card():                                                                        #Cardクラスを定義⇒objectクラスを継承している(特殊メソッドをインポートできる)
    suits = ["spades", "hearts", "diamonds", "clubs"]                                #クラス変数suitsにリスト型オブジェクトを保存⇒全てのカードマークを保存する
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Juck", "Queen", "King", "Ace"]                                                  #クラス変数valuesにリスト型オブジェクトを保存⇒全てのカード番号を保存する

    #ゲームに使用するカードを作成
    def __init__(self, v, s):                                                        #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒１枚のカードを作成する
        self.value = v                                                               #インスタンス変数valueに入力値(引数)vのデータ(値)を保存⇒カード番号を保存する
        self.suit = s                                                                #インスタンス変数suitに入力値(引数)sのデータ(値)を保存⇒カードマークを保存する
    
    #プレイヤー同士のカード番号とマークを比較
    def __lt__(self, c2):                                                            #インスタンスオブジェクトを「<」演算子の被演算子として扱えるように__lt__特殊メソッドをオーバーライド⇒評価結果をTrue or Falseで返す！
        if self.value < c2.value:                                                    #プレイヤー１のカード番号(self.value)が対戦相手(c2.value)より小さい場合
            return True                                                              #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        if self.value == c2.value:                                                   #プレイヤー１のカード番号(self.value)が対戦相手(c2.value)と等価の場合
            if self.suit < c2.suit:                                                  #プレイヤー１のカードマーク(self.suit)が対戦相手(c2.suit)より小さい場合
                return True                                                          #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義
            else:
                return False                                                         #False評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義
        return False                                                                 #全てのif条件式がFlase評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義⇒プレイヤー１のカード番号のほうが大きい！　/　Cardクラスで作成したインスタンスオブジェクトが「<」演算子の被演算子として使用された場合に__lt__特殊メソッドが呼び出される！

    def __gt__(self, c2):                                                            #インスタンスオブジェクトが「>」演算子の被演算子として扱えるように__gt__特殊メソッドをオーバーライド⇒評価結果をTrue or Falseで返す！
        if self.value > c2.value:                                                    #プレイヤー１のカード番号(self.value)が対戦相手(c2.value)より大きい場合
            return True                                                              #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        if self.value == c2.value:                                                   #プレイヤー１のカード番号(self.value)が対戦相手(c2.value)と等価の場合
            if self.suit > c2.suit:                                                  #プレイヤー１のカードマーク(self.suit)が対戦相手(c2.suit)より大きい場合
                return True                                                          #if条件式がTrue評価の場合はブール型オブジェクトTrueを出力値(戻り値)として定義
            else:
                return False                                                         #False評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義
        return False                                                                 #全てのif条件式がFalse評価の場合はブール型オブジェクトFalseを出力値(戻り値)として定義⇒プレイヤー１のカード番号のほうが小さい！　/　Cardクラスで作成したインスタンスオブジェクトが「>」演算子の被演算子として使用された場合に__gt__特殊メソッドが呼び出される！
    
    #プレイヤーカードの番号とマークを文字列で出力
    def __repr__(self):                                                              #インスタンスオブジェクトを文字列化する為に__repr__特殊メソッドをオーバーライド
        v = Card.values[self.value] + " of " + Card.suits[self.suit]                 #Cardクラスを通してクラス変数valuesとsuitsからインデックス値(self.value, self.suit)に該当するオブジェクト(要素)を取得して変数vに保存
        return v                                                                     #変数vのデータ(値)を出力値(戻り値)として定義　/　インスタンスオブジェクトを文字列として扱う場合に__repr__特殊メソッドが呼び出される！

"""
card1 = Card(10, 3)                                                                  #Cardクラスを使用してインスタンスオブジェクトを作成して変数card1に保存
card2 = Card(13, 1)                                                                  #Cardクラスを使用してインスタンスオブジェクトを作成して変数card2に保存
print(card1 < card2)                                                                 #インスタンスオブジェクトcard1を通して__lt__特殊メソッドを呼び出して入力値(引数)にインスタンスオブジェクトcard2を渡す⇒card1.__lt__(card2)
print(card1 > card2)                                                                 #インスタンスオブジェクトcard1を通して__gt__特殊メソッドを呼び出して入力値(引数)にインスタンスオブジェクトcard2を渡す⇒card1.__gt__(card2)
print(card1)                                                                         #インスタンスオブジェクトcard1を文字列として出力⇒card1.__repr__()
print(card2)                                                                         #インスタンスオブジェクトcard2を文字列として出力⇒card2.__repr__()
"""

#デッキ
class Deck():                                                                        #Deckクラスを定義⇒objectクラスを継承している(特殊メソッドをオーバーライドできる)
    #５２枚のカードデッキを作成
    def __init__(self):                                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒５２枚のカードデッキを作成する
        self.list_cards = []                                                         #インスタンス変数list_cardsに空のリスト型オブジェクトを保存⇒Cardクラスで作成したインスタンスオブジェクトを１個ずつ保存する
        for i in range(2, 15):                                                       #変数iにカード番号(values)のインデックス値をイテラブルなオブジェクトとして１個ずつ割り当てる
            for j in range(4):                                                       #変数jにカードマーク(suits)のインデックス値をイテラブルなオブジェクトとして１個ずつ割り当てる
                self.list_cards.append(Card(i, j))                                   #appendメソッドを使用して空のリスト型オブジェクト(self.list_cards)にCardクラスで作成したインスタンスオブジェクトを追加⇒２重ループ処理が終了すると５２枚のカードデッキが完成する！
        shuffle(self.list_cards)                                                     #２重ループが終了した後にshuffleメソッドを使用してデッキをランダムに並び替える
    
    #対戦に使用したカードをデッキ内から削除
    def rm_card(self):                                                               #パブリックメソッドを定義
        if len(self.list_cards) == 0:                                                #カードデッキの枚数がゼロの場合
            return None                                                              #if条件式がTrue評価の場合はNone型オブジェクトを出力値(戻り値)として定義⇒False評価の場合は次のコードを実行する
        return self.list_cards.pop()                                                 #カードデッキ(self.list_cards)に対してpopメソッドを使用して対戦に使用したカードの要素を削除して、そのカードの番号(value)とマーク(suit)を取得して出力値(戻り値)として定義⇒デッキから１枚カードが減る

"""
deck = Deck()                                                                        #Deckクラスを使用してインスタンスオブジェクトを作成して変数deckに保存
for card in deck.list_cards:                                                         #インスタンスオブジェクトdeckを通してカードデッキ(self.list_cards)を取得してイテラブルなオブジェクトとして変数cardに１個ずつ割り当てる
    print(card)
print(len(deck.list_cards))

print(deck.list_cards)
print(len(deck.list_cards))
deck.rm_card()                                                                       #インスタンスオブジェクトdeckを通してrm_cardsメソッドを呼び出す⇒対戦に使用したカード番号(value)とマーク(suit)を取得してデッキ(self.list_cards)から削除する
print(len(deck.list_cards))
print(deck.rm_card())
"""

#プレイヤー
class Player():                                                                      #Playerクラスを定義⇒objectクラスを継承している(特殊メソッドをオーバーライドできる)
    #プレイヤーの初期状態を作成
    def __init__(self, name):                                                        #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒プレイヤーの初期状態を作成する
        self.wins = 0                                                                #インスタンス変数winsに整数型オブジェクト0を保存⇒ラウンド毎の勝利回数を数える
        self.card = None                                                             #インスタンス変数cardにNone型オブジェクトを保存⇒プレイヤーが持っているカードを保存する
        self.name = name                                                             #インスタンス変数nameに入力値(引数)nameのデータ(値)を保存⇒プレイヤー名を保存する

"""
player = Player("Monta")                                                             #Playerクラスを使用してインスタンスオブジェクトを作成して変数playerに保存
print(player.wins, player.card, player.name)
"""

class Game():                                                                        #Gameクラスを定義⇒objectクラスを継承している(特殊メソッドをオーバーライドできる)
    #カードデッキとプレイヤーの初期状態を作成
    def __init__(self):                                                              #インスタンスオブジェクトを作成する為の特殊メソッドを定義⇒カードデッキとプレイヤーを用意する
        name1 = input("Enter name of player1: ")                                     #変数name1にinput関数の文字列型オブジェクト出力値(戻り値)を保存⇒プレイヤー１の名前を保存する
        name2 = input("Enter name of player2: ")                                     #変数name2にinput関数の文字列型オブジェクト出力値(戻り値)を保存⇒プレイヤー２の名前を保存する
        self.deck = Deck()                                                           #インスタンス変数deckにDeckクラスのインスタンスオブジェクトを保存⇒５２枚のカードデッキを保存する
        self.p1 = Player(name1)                                                      #インスタンス変数p1にPlayerクラスのインスタンスオブジェクトを保存⇒プレイヤー１の初期状態を保存する
        self.p2 = Player(name2)                                                      #インスタンス変数p2にPlayerクラスのインスタンスオブジェクトを保存⇒プレイヤー２の初期状態を保存する
    
    #ラウンド毎の勝利プレイヤーを表示
    def wins(self, winner):                                                          #パブリックメソッドを定義
        print("The winner is {}!".format(winner))                                    #formatメソッドを使用して書式化文字列を入力値(引数)winnerに置き換える
    
    #プレイヤーの手札を表示
    def draw(self, p1n, p1c, p2n, p2c):                                              #パブリックメソッドを定義
        print("The card of {} is {}! The card of {} is {}".format(p1n, p1c, p2n, p2c))
    
    #ゲーム実行
    def play_game(self):                                                             #パブリックメソッドを定義
        #カードデッキを用意
        cards = self.deck.list_cards                                                 #変数cardsにインスタンスオブジェクトdeckを通してDeckクラスのインスタント変数list_cardsを保存⇒ゲームに使用するカードデッキを用意

        #ラウンドの開始終了を制御
        print("Let's start War Game!!")
        while len(cards) >= 2:                                                       #カードデッキの枚数が２枚未満になるまでループ処理を継続
            game = input("Enter q to suit, another to continue!!")                   #変数gameにinput関数の文字列型オブジェクト出力値(戻り値)を保存
            if game == "q":                                                          #変数gameのデータ(値)が文字列型オブジェクト「q」と等価の場合
                break                                                                #if条件式がTrue評価の場合はbrekaキーワードを使用してwhileループ処理を終了⇒対戦を終了して勝敗判定を行う
        
            #プレイヤーの手札と名前を取得して表示
            p1c = self.deck.rm_card()                                                #インスタンスオブジェクトdeckを通してDeckクラスのrm_cardメソッドを呼び出す⇒プレイヤーの手札の番号(value)とマーク(suit)を取得して、そのカードをデッキから削除する
            p1n = self.p1.name                                                       #インスタンスオブジェクトp1を通してPlayerクラスのインスタンス変数nameを取得⇒プレイヤー１の名前を保存する
            p2c = self.deck.rm_card()                                                #インスタンスオブジェクトdeckを通してDeckクラスのrm_cardメソッドを呼び出す⇒プレイヤー２の手札の値(value)とマーク(suit)を取得して、そのカードをデッキから削除する
            p2n = self.p2.name                                                       #インスタンスオブジェクトp2を通してPlayerクラスのインスタンス変数nameを取得⇒プレイヤー２の名前を保存する
            self.draw(p1n, p1c, p2n, p2c)                                            #drawメソッドを呼び出してプレイヤーの名前と手札を入力値(引数)として渡す⇒プレイヤーの名前と手札が表示される

            #ラウンド毎の勝利プレイヤーを表示
            if p1c > p2c:                                                            #プレイヤー１の手札(p1c)が対戦相手(p2c)より大きい場合
                self.p1.wins += 1                                                    #if条件式がTrue評価の場合はインスタンスオブジェクトp1を通してPlayerクラスのインスタンス変数winsをインクリメントして再保存⇒プレイヤー１の勝利回数が増える！
                self.wins(p1n)                                                       #if条件式がTrue評価の場合はwinsメソッドを呼び出してプレイヤー１の名前を入力値(引数)として渡す
            else:
                self.p2.wins += 1                                                    #Flase評価の場合はインスタンスオブジェクトp2を通してインスタンス変数winsをインクリメントして再保存⇒プレイヤー２の勝利回数が増える
                self.wins(p2n)                                                       #Flase評価の場合はwinsメソッドを呼び出してプレイヤー２の名前を入力値(引数)として渡す

        #勝利プレイヤーを表示
        w = self.winner(self.p1, self.p2)                                            #winnerメソッドを呼び出す⇒入力値(引数)にPlayerクラスのインスタンスオブジェクトself.p1, self.p2を渡す = winnerメソッド内でPlayerクラス内のインスタンス変数やメソッドを使用できるようになる！
        print("The game is over, winner is {}!!".format(w))                          #formatメソッドを使用して書式化文字列を変数wのデータ(値)に置き換える

    #プレイヤーの勝利回数を判定
    def winner(self, p1, p2):                                                        #パブリックメソッドを定義⇒入力値(引数)にインスタンスオブジェクトself.p1, self.p2を受け取る = コンポジション
        if p1.wins > p2.wins:                                                        #プレイヤー１の勝利回数(p1.wins)が対戦相手(p2.wins)より大きい場合
            return p1.name                                                           #インスタンスオブジェクトp1を通してPlayerクラスのインスタンス変数nameのデータ(値)を取得して出力値(戻り値)として定義⇒プレイヤー１の名前が表示される
        if p1.wins < p2.wins:                                                        #プレイヤー１の勝利回数(p1.wins)が対戦相手(p2.wins)より小さい場合
            return p2.name                                                           #if条件式がTrue評価の場合はインスタンスオブジェクトp2を通してPlayerクラスのインスタンス変数nameのデータ(値)を取得して出力値(戻り値)として定義⇒プレイヤー２の名前が出力される
        return "Draw"                                                                #全てのif条件式がFalse評価の場合は文字列型オブジェクト「Draw」を出力値(戻り値)として定義

game = Game()                                                                        #Gameクラスを使用してインスタンスオブジェクトを作成して変数gameに保存
game.play_game()                                                                     #インスタンスオブジェクトgameを通してplay_gameメソッドを呼び出す

# <War(戦争)>_Review
from random import shuffle

#カード
class Card():
    #カード情報(番号&マーク)
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Juck", "Queen", "King", "Ace"]

    #カード単体を作成
    def __init__(self, v, s):
        self.value = v
        self.suit = s
    
    #手札のカード番号とマークを「<」演算子で比較
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit                                                #プレイヤー１のマーク(self.suit)とプレーヤー２のマーク(c2.suit)を「<」演算子で比較して評価判定(Treu or False)を出力値(戻り値)として定義
        return False
    
    #手札のカード番号とマークを「>」演算子で比較
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit                                                #プレイヤー１のマーク(self.suit)とプレイヤー２のマーク(c2.suit)を「>」演算子で比較して評価判定(True or False)を出力値(戻り値)として定義
        return False
    
    #手札のカード番号とマークを文字列として出力
    def __repr__(self):
        card_print = Card.values[self.value] + " of " + Card.suits[self.suit]
        return card_print

#デッキ
class Deck():
    #５２枚のカードデッキを作成
    def __init__(self):
        self.list_cards = []
        for i in range(2, 15):
            for j in range(4):
                self.list_cards.append(Card(i, j))
        shuffle(self.list_cards)
    
    #デッキの枚数を判定して１枚以上の場合は１枚減らして、減らしたカードの番号とマークを取得
    def draw(self):
        if self.list_cards == 0:
            return None
        return self.list_cards.pop()

"""
deck = Deck()
for card in deck.list_cards:
    print(card)
print(len(deck.list_cards))
deck.rm_cards()
print(len(deck.list_cards))
print(deck.rm_cards())
"""

#プレイヤー
class Player():
    #プレイヤーの初期情報を作成
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

#ゲーム
class Game():
    #カードデッキとプレイヤーの初期情報を用意
    def __init__(self):
        name1 = input("Enter player1's name: ")
        name2 = input("Enter player2's name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    #ラウンド毎の勝利プレイヤーを表示
    def print_winner(self, winner):                                                        #入力値(引数)winnerはPlayerクラスのインスタンスオブジェクトを受け取る(コンポジション)⇒Playerクラスのインスタンス変数とメソッドを取得することができる
        w = "{} win this round!"
        print(w.format(winner.name))
    
    #プレイヤーの手札を表示
    def print_draw(self, p1, p2):                                                          #入力値(引数)p1,p2はPlayerクラスをインスタンスオブジェクトを受け取る(コンポジション)⇒Playerクラスのインスタンス変数とメソッドを取得できる
        d = "{}'s card is {}, {}'s card is {}!!"
        print(d.format(p1.name, p1.card, p2.name, p2.card))
    
    #ゲーム実行
    def play_game(self):
        #カードデッキを用意
        card_deck = self.deck.list_cards
        print("Let's start war game!")

        #ゲームの開始終了を制御
        while len(card_deck) >= 2:
            #ゲーム継続と終了を決定
            response = input("Enter q to quit, another to continue!")
            if response == "q":
                break

            #プレイヤーの手札と名前を取得して表示
            self.p1.card = self.deck.draw()                                                #Playerクラスのインスタンスオブジェクトp1のインスタンス変数cardにDeckクラスのdrawメソッドの出力値(戻り値)を保存⇒プレイヤーの手札の番号とマークが保存される
            self.p2.card = self.deck.draw()                                                #Playerクラスのインスタンスオブジェクトp2の同上
            self.print_draw(self.p1, self.p2)

            #ラウンド毎の勝利プレイヤーを表示
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
        
        #勝利プレイヤーを表示
        winner = self.winner(self.p1, self.p2)
        print(winner)
    
    #ラウンドの勝利回数から勝利プライヤーを判定
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return "The winner is {}!!".format(p1.name)
        if p1.wins < p2.wins:
            return "The winner is {}!!".format(p2.name)
        return "This game is draw!!"

game = Game()
game.play_game()

# <War(戦争)>_review
from random import shuffle

#カード
class Card():
    #カード情報を用意(クラス変数)
    suits = ["spades", "hearts", "diamonds", "culbs"]
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Juck", "Queen", "King", "Ace"]                                                             #カード番号とインデックス値を一致させる為に２つのNone型オブジェクトを追加

    #カード単体を作成
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    #カードの番号とマークを「<」演算子で比較
    def __lt__(self, card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:                                                            #プレイヤー１の番号(self.value)と対戦相手(card2.value)が等価の場合
            return self.suit < card2.suit                                                        #プレイヤー１のマーク(self.suit)と対戦相手(card2.suit)を比較して評価結果を出力値(戻り値)として定義
        return False
    
    #カードの番号とマークを「>」演算子で比較
    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:                                                            #プレイヤー１の番号(self.value)と対戦相手(card2.value)が等価の場合
            return self.suit > card2.suit                                                        #プレイヤー１のマーク(self.suit)と対戦相手(card2.suit)を比較して評価結果を出力値(戻り値)として定義
        return False
    
    #カードの番号とマークを文字列として出力
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]                          #クラス変数(values, suits)を取得してインスタンス変数(value, suit)に該当するインデックス値のオブジェクト(要素)を取得
"""
card1 = Card(10, 0)
card2 = Card(13, 3)
print(card1)                                                                                     #インスタンスオブジェクトcard1を文字列として扱う為に__repr__特殊メソッドをオーバーライド⇒card1.__repr__()
print(card2)                                                                                     #インスタンスオブジェクトcard2を文字列として扱う為に__repr__特殊メソッドをオーバーライド⇒card2.__repr__()
print(card1 < card2)                                                                             #インスタンスオブジェクトcard1とcard2を比較演算子の被演算子として扱う為に__lt__特殊メソッドをオーバーライド⇒card1.__lt__(card2)
print(card1 > card2)                                                                             #インスタンスオブジェクトcard1とcard2を比較演算子の被演算子として扱う為に__gt__特殊メソッドをオーバーライド⇒card1.__gt__(card2)
"""

#デッキ
class Deck():
    #カードデッキの入れ物を用意(クラス変数)
    list_cards = []

    #５２枚のカードデッキを作成
    def __init__(self):
        for i in range(2, 15):
            for j in range(4):
                self.list_cards.append(Card(i, j))                                               #Cardクラスを使用してインスタンスオブジェクトを作成してクラス変数list_cardsに追加⇒５２枚のカードを追加する
        shuffle(self.list_cards)                                                                 #shuffleメソッドを使用してクラス変数list_cardsのオブジェクト(要素)をランダムに並び替える
    
    #デッキの内のカード枚数を判定
    #１枚以上の場合はカードを１枚削除して、そのカードの番号とマークを取得
    def draw(self):
        if len(self.list_cards) == 0:
            return None
        return self.list_cards.pop()                                                             #popメソッドを使用してクラス変数list_cardsの最後のオブジェクト(要素)を削除して、そのデータ(値)を取得⇒デッキからカードを１枚減らして、手札の番号とマークを取得する
"""
deck = Deck()
for card in deck.list_cards:                                                                     #インスタンスオブジェクトdeckを通してクラス変数list_cardsを取得してイテラブルなオブジェクトとして変数cardに１個ずつ割り当てる
    print(card)
print(len(deck.list_cards))
card = deck.draw()                                                                               #インスタンスオブジェクトdeckを通してdrawメソッドを呼び出す⇒デッキからカードを１枚減らして、そのカードの番号とマークを手札情報として取得する
print(card)
print(len(deck.list_cards))
"""

#プレイヤー
class Player():
    #プレイヤーの初期状態を作成
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
"""
player = Player("Monta")
print(player.wins, player.card, player.name)
"""

#ゲーム
class Game():
    #カードデッキとプレイヤーの初期情報を作成
    def __init__(self):
        self.deck = Deck()
        name1 = input("Enter player1's name: ")
        name2 = input("Enter player2's name: ")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    #ラウンド毎の勝利プレイヤーを表示
    def print_winner(self, winner):                                                               #入力値(引数)winnerにPlayerクラスのインスタンスオブジェクトを渡す = コンポジション
        win = "{} wins this round!!"
        print(win.format(winner.name))                                                            #インスタンスオブジェクトwinnerを通してインスタンス変数nameのデータ(値)を参照
    
    #プレイヤーが引いたカードの番号とマークを表示
    def print_draw(self, p1, p2):                                                                 #入力値(引数)p1とp2にPlayerクラスのインスタンスオブジェクトを渡す = コンポジション
        card = "{}'s card is {}, {}'s card is {}!!"
        print(card.format(p1.name, p1.card, p2.name, p2.card))                                    #インスタンスオブジェクトp1とp2を通してインスタンス変数nameとcardのデータ(値)を参照
    
    #ラウンドの勝利回数から勝利プレイヤーを判定
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        else:
            return "This game is draw!!"
    
    #ゲーム実行
    def play_game(self):
        #カードデッキを用意
        cards = self.deck
        print("Let's play War Game!!")

        #ラウンドの終了開始を制御
        while len(cards.list_cards) >= 1:
            #ゲーム終了と継続を確認
            response = input("Enter q to quit, another to continue: ")
            if response == "q":
                break

            #プレイヤーの手札と名前を表示
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)

            #ラウンド毎の勝利プレイヤーを表示
            if self.p1.card > self.p2.card:                                                         #インスタンスオブジェクトp1とp2を「>」演算子の被演算子として扱う為、__gt__特殊メソッドをオーバーライド
                self.p1.wins += 1
                self.print_winner(self.p1)                                                          #print_wiinerメソッドを呼び出して入力値(引数)にインスタンスオブジェクトp1を渡す = コンポジション
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)                                                          #print_winnerメソッドを呼び出して入力値(引数)にインスタンスオブジェクトp2を渡す = コンポジション
        
        #勝利プレイヤーを表示
        game_winner = self.winner(self.p1, self.p2)                                                 #winnerメソッドを呼び出して入力(引数)にインスタンスオブジェクトp1とp2を渡す = コンポジション
        print("Game is over!! The winner is {}!!".format(game_winner))

game = Game()
game.play_game()

# <War(戦争)>_review
from random import shuffle

#カード
class Card():
    #カード情報(クラス変数)
    suits = ["spades", "hearts", "diamonds", "culbs"]
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Juck","Queen", "King", "Ace"]

    #カード作成(インスタンスオブジェクトを作成)
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    #カードの番号とマークを「<」 演算子で比較(__lt__特殊メソッドをオーバーライド)
    def __lt__(self, player2):
        if self.value < player2.value:
            return True
        if self.value == player2.value:
            return self.suit < player2.suit
        return False
    
    #カード番号とマークを「>」演算子で比較(__gt__特殊メソッドをオーバーライド)
    def __gt__(self, player2):
        if self.value > player2.value:
            return True
        if self.value == player2.value:
            return self.suit > player2.suit
        return False
    
    #カードの番号とマークを文字列として出力(__repr__特殊メソッドをオーバーライド)
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]
"""
card1 = Card(10, 1)
card2 = Card(13, 3)
print(card1)
#⇒card1.__repr__()
print(card2)
#⇒card2.__repr__()
print(card1 < card2)
#⇒card1.__lt__(card2)
print(card1 > card2)
#⇒card1.__gt__(card2)
"""

#カード
class Deck():
    #カードデッキの格納先(クラス変数)
    cards_list = []

    #５２枚のカードデッキを作成(インスタンスオブジェクトを作成)
    def __init__(self):
        for i in range(2, 15):
            for j in range(4):
                self.cards_list.append(Card(i, j))
        shuffle(self.cards_list)

    #デッキ内のカード枚数を判定して１枚以上の場合は、そのカード番号とマークを取得してデッキ内から削除
    def draw(self):
        if len(self.cards_list) == 0:
            return None
        return self.cards_list.pop()
"""
deck = Deck()
for card in deck.cards_list:
    print(card)
print(len(deck.cards_list))
print(deck.draw())
print(len(deck.cards_list))
"""

#プレイヤー
class Player():
    #プレイヤーの初期設定を作成(インスタンスオブジェクトを作成)
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
"""
player1 = Player("Monta")
print(player1.wins, player1.card, player1.name)
"""

#ゲーム
class Game():
    #カードデッキとプレイヤーの初期情報を作成(インスタンスオブジェクトを作成)
    def __init__(self):
        self.deck = Deck()
        name1 = input("Enter name of Player1's name: ")
        name2 = input("Enter name of Player2's name: ")
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    
    #ラウンド毎の勝利プレイヤーを表示
    def print_wins(self, winner):
        print("The winner of this raound {}!!".format(winner.name))
    
    #プレイヤーが引いたカードを表示
    def print_draw(self, player1, player2):
        print("{}'s card is {}, {}'s card is {}!!".format(player1.name, player1.card, player2.name, player2.card))
    
    #ラウンドの勝利回数からゲームの勝利プレイヤーを表示
    def game_winner(self, player1, player2):
        if player1.wins > player2.wins:
            return "The game is over, the winner is {}!!".format(player1.name)
        elif player1.wins < player2.wins:
            return "The game is over, the winner is {}!!".format(player2.name)
        else:
            return "This game is draw!!"
    
    #ゲームを制御
    def play_game(self):
        #カードデッキを用意
        use_deck = self.deck.cards_list
        print("Let's play War Game!!")
        #ラウンドの開始終了を制御
        while len(use_deck) >= 1:
            #ゲーム終了と継続を決定
            request = input("Enter q to quit, another to continue!")
            if request =="q":
                break
            #各プレイヤーの名前と手札を表示(print_drawメソッドとDeckクラスのdrawメソッドを使用)
            self.player1.card = self.deck.draw()
            self.player2.card = self.deck.draw()
            self.print_draw(self.player1, self.player2)
            #ラウンド毎の勝利プレイヤーを表示(print_winsメソッドを使用)
            if self.player1.card > self.player2.card:
                self.player1.wins += 1
                self.print_wins(self.player1)
            else:
                self.player2.wins += 1
                self.print_wins(self.player2)
        #ゲーム勝利プレイヤーを表示
        result = self.game_winner(self.player1, self.player2)
        print(result)

game = Game()
game.play_game()
