# 知識を１つにまとめる

#ウェブスクレイパー
import urllib.request                                                           #urllib.requestモジュールをインポート
from bs4 import BeautifulSoup                                                   #BeautifulSoup4モジュールからBeautifulsoupメソッドをインポート

class Scraper():                                                                #Scraperクラスを定義(クラスオブジェクトを継承している=特殊メソッドをオーバーライド可能)
    def __init__(self, site):                                                   #スクレイピング対象のサイトURLを入力値(引数)として受け取る⇒インスタンスオブジェクトを作成する為の特殊メソッドを定義
        self.site = site                                                        #スクレイピング対象のサイトURLを保存⇒インスタンス変数siteに入力値(引数)siteのデータ(値)を保存
    
    def scrape(self):                                                           #スクレイピングを実行したい時に使用⇒プライベートメソッドを定義(=インスタンスオブジェクトを通してのみクラス外から参照可能)
        r = urllib.request.urlopen(self.site)                                   #urlopenメソッドを使用してスクレイピング対象のサイトURL(self.site)のHTMLと追加情報を取得してレスポンスオブジェクトとして変数rに保存⇒urllib.requestモジュールを通してurlopen関数を呼び出す
        html = r.read()                                                         #レスポンスオブジェクトに対してreadメソッドを使用して保存されたHTMLデータを出力して変数htmlに保存
        parser = "html.parser"                                                  #BeautifulSopuメソッドにスクレイピング対象のサイトURLのHTMLをパースすることを伝える⇒変数parserに文字列型オブジェクトを保存
        sp = BeautifulSoup(html, parser)                                        #BeautifulSopuメソッドを使用してスクレイピング対象のサイトURLのHTMLデータをパースしてBeautifulSopuオブジェクトとして変数spに保存⇒BeautifulSoupメソッドの出力値(戻り値)を変数spに保存
        for tag in sp.find_all("a"):                                            #Beautifulオブジェクトに対してfind_aalメソッドを使用してHTMLデータの中からリンクタグ(aタグ)を取得してリスト型オブジェクト(イテラブルなオブジェクト)として変数tagに１つずつ割り当てる
            url = tag.get("href")                                               #tagオブジェクト(aタグ)に対してgetメソッドを使用してhref属性のデータ(値)を取得して変数urlに保存
            if url is None:                                                     #変数urlのデータ(値)がNone型オブジェクト同じの場合
                continue                                                        #if条件式がTrueの場合はforループ処理を１回スキップ
            if "articles" in url:                                               #変数urlのデータ(値)の中に「articles」が含まれている場合
                print("https://news.google.com/" + url)                         #if条件式がTrue評価の場合はスクレイピング対象のサイトURLと変数URLのデータ(値)を連結して表示

news = "https://news.google.com/"                                               #変数newsにスクレイピング対象のサイトURLを保存
Scraper(news).scrape()                                                          #Scraperクラスを通してインスタンスオブジェクトを作成してscrapeメソッドを呼び出す

# <Googleニュースのスクレイパー>_review
#必要なモジュールとメソッドを用意
import urllib.request                                                           #openurlメソッドを使用するためurllib.requestモジュールをインポート
from bs4 import BeautifulSoup                                                   #HTMLデータのパース(構造)を行うためBeaitufulSoup4モジュールからBeautifulSoupメソッドをインポート

#スクレイピングを行うクラスを定義
class Scraper():                                                                #スクレイピング処理を行うScraperクラスを定義⇒Pythonの全てのクラスはクラスオブジェクトを継承している(=特殊メソッドのオーバーライドが可能)
    #インスタンスオブジェクトを作成
    def __init__(self, site):                                                   #スクレイピング対象のサイトURLを保持
        self.site = site                                                        #インスタンス変数siteにスクレイピング対象のサイトURLを保存

    #スクレイピング処理を実行
    def scrape(self):                                                           #プライベートメソッドを定義
        #HTMLデータを取得
        request = urllib.request.urlopen(self.site)                             #urlopenメソッドを使用してスクレイピング対象のウェブサイト(self.site)のHTMLデータを取得してResponseオブジェクトとして変数requestに保存
        #HTMLデータを出力
        html = request.read()                                                   #Responseオブジェクトrequestに対してreadメソッドを使用して取得したHTMLデータを出力して変数htmlに保存
        #利用するパーサーを指定
        parse = "html.parser"                                                   #利用するパーサーを指定する為に変数parseにパーサー(html.parser)を保存
        #HTMLデータをパース(構造化)
        sp = BeautifulSoup(html, parse)                                         #BeautifulSoupメソッドを使用して出力したHTMLデータ(html)をパース(構造化)してBeautifulSoupオブジェクトとして変数spに保存
        #スクレイピング処理を制御
        for tag in sp.find_all("a"):                                            #BeaituifuSoupオブジェクトspに対してfind_allメソッドを使用して全てのリンクタグ(aタグ)を取得してリスト型オブジェクトに保存、forループ処理を使用してイテラブルなオブジェクトとして変数tagに１つずつ割り当てる
            url = tag.get("href")                                               #割り当てられたリンクタグ(tag)に対してgetメソッドを使用してhref属性のURLを取得して変数urlに保存
            if url is None:                                                     #URLがNone型オブジェクトと同じ場合
                continue                                                        #if条件式がTrue評価の場合はforループ処理を１回スキップ⇒Fasle評価の場合は次の処理を実行
            if "articles" in url:                                               #URLの中らに文字列「articles」が含まれている場合
                print(self.site + url)                                          #if条件式がTrue評価の場合はスクレイピング対象のサイトURL(self.site)とhref属性のURL(url)を連結して出力

news = "https://news.google.com/"                                               #スクレイピング対象のサイトURLを変数newsに保存⇒インスタンスオブジェクトに保持される！
Scraper(news).scrape()                                                          #Scraperクラスを使用してインスタンスオブジェクト作成してscrapeメソッドを呼び出す

# <チャレンジ>
#問題1
import urllib.request                                                           #urllib.requestモジュールをインポート⇒urlopenメソッドを使用してスクレイピング対象のウェブサイトのHTMLデータを取得する！
from bs4 import BeautifulSoup                                                   #BeautifulSoup4モジュールからBeautifulSoupメソッドをインポート⇒取得したHTMLデータをパース(構文解析)する！

class Scraper():                                                                #Scraperクラスを定義(objectクラスを継承)⇒ウェブスクレイピングを行う機能を持つ！
    #スクレイピング対象のサイトURLを保持
    def __init__(self,site):
        self.site = site                                                        #インスタンス変数siteを定義⇒入力値(引数)に受け取ったサイトURLを保存する！
    
    #スクレイピングを制御
    def scrape(self):
        #スクレイピング対象のウェブサイトのHTMLデータを取得
        request = urllib.request.urlopen(self.site)                             #urlopenメソッドを使用⇒HTMLデータを取得してResponseオブジェクトとして変数requestに保存する！
        #HTMLデータを出力
        html = request.read()                                                   #Responseオブジェクトに対してreadメソッドを使用⇒Responseオブジェクトに保存されたHTMLデータを出力して変数htmlに保存する！
        #HTMLデータをパース(構文解析)
        sp = BeautifulSoup(html, "html.parser")                                 #BeautifulSoupメソッドを使用⇒HTMLデータをパース(構文解析)してBeautifulSoupオブジェクトとして保存する！
        #スクレイピング処理を制御
        url_list = []                                                           #変数url_listに空のリスト型オブジェクトを保存⇒取得したhref属性のデータ(値)を格納する！
        for tag in sp.find_all("a"):                                            #BeautifulSoupオブジェクトに対してfind_allメソッドを使用⇒パース(構文解析)済のHTMLデータの中からリンクタグ(aタグ)を取得してリスク型オブジェクトとして保存してイテラブルなオブジェクトとして変数tagに１つずつ割り当てる！
            #リンクタグ(aタグ)からhref属性のデータ(値)を取得
            url = tag.get("href")                                               #リンクタグ(tag)に対してgetメソッドを使用⇒リンクタグ内のhref属性のデータ(値)を取得して変数urlに保存
            #href属性のデータ(値)に応じて分岐処理
            if url is None:                                                     #href属性(url)がNone型オブジェクトと同じの場合
                continue                                                        #if条件式がTrue評価の場合はforループ処理を１回スキップ
            if "articles" in url:                                               #href属性(url)の中に「articles」を含む場合
                news_url = "\n" + self.site + url                               #if条件式がTrue評価の場合は改行コード(\n)とスクレイピング対象のサイトURL(self.site)とhref属性(url)を連結して変数news_urlに保存
                url_list.append(news_url)                                       #リスト型オブジェクトurl_listに対してappendメソッドを使用⇒連結したURLをリストに追加する！
        #URLリストを書き出して保存
        with open("st.txt", "w") as f:                                          #with構文でopenメソッドを使用⇒書き込みモード(w)でテキストファイル(st.txt)を作成してファイルオブジェクトとして変数fに保存
            for i in url_list:                                                  #ニュースURLを格納したリスト(url_list)をイテラブルなオブジェクトとして変数iに１つずつ割り当てる
                f.write(i)                                                      #ファイルオブジェクトfに対してwriteメソッドを使用して変数iに割り当てたニュースURLを書き込む⇒forループ処理が完了した時点で全てのニュースURLがテキストファイルに書き込まれている！

news = "https://news.google.com/"                                               #変数newsにスクレイピング対象のサイトURLを保存
Scraper(news).scrape()                                                          #Scraperクラスを使用してインスタンスオブジェクトを作成してscrapeメソッドを呼び出す！

#問題1(解答例)
#必要なモジュールとメソッド
import urllib.request                                                           #urllib.requestモジュールをインポート⇒urlopenメソッドを使用してスクレイピング対象のウェブサイトのHTMLデータを取得する！
from bs4 import BeautifulSoup                                                   #BeautifulSoup4モジュールからBeautifulSoupメソッドをインポート⇒HTMLデータをパース(構文解析)する！

#スクレイピングするクラスを定義
class Scraper():                                                                #Scraperクラスを定義(objectクラスを継承)
    #スクレイピング対象のサイトURLを保持
    def __init__(self, site):                                                   #__init__特殊メソッドをオーバーライド
        self.site = site                                                        #入力値(引数)として受け取ったサイトURLをインスタンス変数siteに保存⇒スクレイピング対象のサイトURLを保持する！
    
    #スクレイピングを制御
    def scrape(self):
        #HTMLデータを取得
        response = urllib.request.urlopen(self.site)                            #urlopenメソッドを使用⇒スクレイピング対象のウェブサイト(self.site)からHTMLデータを取得してResponseオブジェクトとして変数responseに保存する！
        #HTMLデータを読込
        html = response.read()                                                  #Responseオブジェクトに対してreadメソッドを使用⇒取得したHTMLデータを読み込んで変数htmlに保存する！
        #HTMLデータをパース(構文解析)
        sp = BeautifulSoup(html, "html.parser")                                #Beautifulメソッドを使用⇒読み込んだHTMLデータ(html)をパース(構文解析)してBeautifulSoupオブジェクトとして変数spに保存する！
        #URLを外部ファイルに書き込む
        with open("output.txt", "w") as f:                                      #with構文とopen関数をして書き込み先ファイルを作成してテキストオブジェクトとして変数fに保存
            #スクレイピング処理を制御
            for tag in sp.find_all("a"):                                        #forループ処理を実行⇒BeautifulSoupオブジェクトに対してfind_allメソッドを使用してパース(構文解析)済のHTMLデータからリンクタグ(aタグ)を取得してリスト型オブジェクトに保存してイテラブルなオブジェクトとして変数tagに１つずつ割り当てる！
                url = tag.get("href")                                           #取得したリンクタグ(aタグ)に対してgetメソッドを使用⇒href属性のデータ(値)を取得して変数urlに保存する！
                if url is None:                                                 #href属性のデータ(値)がNone型オブジェクトと同じ場合
                    continue                                                    #if条件文がTrue評価の場合はforループ処理を１回スキップ
                if "articles" in url:                                           #href属性のデータ(値)に文字列「articles」が含まれている場合
                    news_url = "\n" + self.site + url                           #if条件式がTrue評価の場合は改行コード(\n)とスクレイピング対象のサイトURL(self.site)とhref属性(urlのデータ(値)を連結して変数news_urlに保存
                    f.write(news_url)                                           #テキストオブジェクトfに対してwriteメソッドを使用⇒各ニュースのURLが書き込み先ファイルへ書き込みされる！(forループ処理が完了すると全てのニュースURLが書き込みされる)

news = "https://news.google.com/"                                               #変数newsにスクレイピング対象のサイトURLを保存
Scraper(news).scrape()                                                          #Scraperクラスを使用してインスタンスオブジェクトを作成してscrapeメソッドを呼び出す