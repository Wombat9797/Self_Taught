# 正規表現

# <正規表現とPython>
# 正規表現のシンプルマッチをPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

l = "Beautiful is better than ugly."                                                  #変数lに文字列型オブジェクトを保存⇒検索対象のテキストorファイルを指定する
matches = re.findall("Beautiful", l)                                                  #m文字列型オブジェクトlの中から検索正規表現(検索する文字列)「Beautiful」と一致する文字列を検索して出力値(戻り値)として変数matchesに保存⇒第一引数に検索正規表現(検索する文字列)「Beautiful」、第二引数に検索対象のテキストorファイルを指定する

print(matches)

# フラグ(オプション)を指定
import re                                                                             #re(regular expression)モジュールをインポート

l = "Beautiful is better than ugly."                                                  #変数lに文字列型オブジェクトを保存⇒検索対象のテキストorファイルを指定する
matches = re.findall("beautiful", l, re.IGNORECASE)                                   #文字列型オブジェクトlの中から検索正規表現(検索する文字列)「beautiful」と一致する文字列を検索して出力値(戻り値)として変数matchesに保存⇒第一引数に検索正規表現(検索する文字列)「beautiful」、第二引数に検索対象のテキストorファイル、第三引数にフラグを指定する

print(matches)

# 正規表現の前方一致をPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

zen = """Although never is
oftern better than
*right now*.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be good
idea.Namespaces
ara one honking 
grat idea -- let's
do more of those """                                                                  #変数zenに複数行の文字列型オブジェクトを保存

m = re.findall("^If", zen, re.MULTILINE)                                              #複数列の文字列型オブジェクトzenの中から先頭の文字列が「If」と一致する文字列を検索して出力値(戻り値)として変数mに保存⇒第一引数に前方一致の検索正規表現「^If」、第二引数に対象のテキストorファイル、第三引数にMULTILINEフラグを指定する
print(m)

# 正規表現の後方一致をPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

zen = """Although never is
oftern better than
*right now*.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be good
idea.Namespaces
ara one honking 
grat idea -- let's
do more of those"""                                                                   #変数zenに複数行の文字列型オブジェクトを保存

m = re.findall("explain,$", zen, re.MULTILINE)                                        #複数列の文字列型オブジェクトzenの中から終端の文字列が「explain,」と一致する文字列を検索して出力値(戻り値)として変数mに保存⇒第一引数に後方一致の検索正規表現(検索する文字列)「explain,$」、第二引数に対象のテキストorファイル、第三引数にMULTILINEフラグを指定する
print(m)

# 正規表現の複数文字との一致をPyhonで実行
import re                                                                             #re(regular expression)モジュールをインポート

string = "Two too"                                                                    #変数stringに文字列型オブジェクトを保存
m = re.findall("t[wo]o", string, re.IGNORECASE)                                       #文字列型オブジェクトstringの中から先頭が「t」、終端が「o」、中間が「w or o」と一致する文字列を検索して出力値(戻り値)として変数mに保存⇒第一引数に複数文字と一致する検索正規表現「t[wo]o」、第二引数に対象のテキストorファイル、第三引数にIGNORECASEフラグを渡す
print(m)

#正規表現の数値との一致をPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

line = "123 hi 34 hello."                                                             #変数lineに文字列型オブジェクトを保存
m = re.findall("\d", line, re.IGNORECASE)                                             #文字列型オブジェクトlineの中で数値と一致(\d)と一致する文字列を検索して出力値(戻り値)として変数mに保存
print(m)

#非貪欲な繰り返しをPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

t = "__one__ __two__ __three__"                                                       #変数tに文字列型オブジェクトを保存
found = re.findall("__.*?__", t)                                                      #文字列型オブジェクトtの中から、先頭と終端をダブルアンダースコア(__)で囲まれ、かつ出来るだけ少ない文字列を検索して出力値(戻り値)として変数foundに保存
for match in found:                                                                   #イテラブルなオブジェクトfoundのオブジェクト(要素)を１個ずつ変数matchに割り当てる
    print(match)

#非貪欲な繰り返しをPythonで実行
import re                                                                             #re(regualr expression)モジュールをインポート
text = """キリンは大昔から __複数名詞__ の興味の対象でした。キリンは __複数名詞__ 
の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得
したのか説明できません。キリンの身長は __数値__ __単位__ 近くあり、その高さのほどんどは
脚と __体の一部__ によるものです。
"""                                                                                   #変数textに複数列の文字列型オブジェクトを保存

def mad_libs(mls):                                                                    #関数mad_libsを定義
    """
    : param mls : string 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は
    後ろを２つのアンダースコアで挟んでください。ヒントの単語にはアンダースコアは含めない
    で下さい。__hint_hint__はだめです。__hint__はOKです。
    """                                                                               #ドキュメンテーション文字列で関数mad_libsの引数の種類とデータ型と内容を定義

    hints = re.findall("__.*?__", mls)                                                #入力値(引数)mlsの中からアンダースコアで囲まれた最小単位の文字列を検索して出力値(戻り値)として変数hintsに保存
    if hints is not None:                                                             #リスト型オブジェクトhintsがNone型オブジェクトと一致しない場合は後の処理を実行
        for word in hints:                                                            #リスト型オブジェクト(=イテラブル)hintsの要素を１個ずつ変数wordに割り当てる
            q = "{}を入力: ".format(word)                                             #formatメソッドを使用して書式化文字列を変数wordのデータ(値)に置き換える
            new = input(q)                                                            #input関数の文字列型オブジェクト出力値(戻り値)を変数newに保存
            mls = mls.replace(word, new, 1)                                           #変数mlsに対してreplaceメソッドを使用してダブルアンダースコアに挟まれた文字列(word)をユーザーが入力した文字列(new)に置換するして再保存
                                                                                      #forループ処理が終了すると全てのダブルアンダースコアに挟まれた文字列(word)は全てユーザーが入力した文字列(new)に置換した状態になる
        mls = mls.replace("\n", "")                                                   #変数mlsに対してreplaceメソッドを使用して改行文字列(\n)を改行無し文字列("")に置換して再保存⇒変数tetxに保存された複数行の文字列型オブジェクトの改行部分が無くなる！
        print(mls)                                                                    #変数mlsを出力する
    else:                                                                             #if条件式がFalse評価の場合
        print("引数mlsが無効です。")

mad_libs(text)

#エスケープによる検索をPythonで実行
import re                                                                             #re(regular expression)モジュールをインポート

line = "I love $"                                                                     #変数lineに文字列型オブジェクトを保存
m = re.findall("\\$", line, re.IGNORECASE)                                            #文字列型オブジェクトlineの中から「$」記号を検索して出力値(戻り値)として変数mに保存
print(m)

# <チャレンジ>
#問題1
import re                                                                              #re(regualr expression)モジュールをインポート

line = "Although that way may not be obvious at first unless you're Dutch."            #変数lineに文字列型オブジェクトを保存
m = re.findall("Dutch", line, re.IGNORECASE)                                           #文字列型オブジェクトlineの中から文字列Dutchを検索して出力値(戻り値)として変数mに保存⇒フラグIGNORECASEで大文字小文字の区別を無視する
print(m)

#問題2
import re                                                                              #re(regualr expression)モジュールをインポート

line = "Arizona 479, 501, 870. California 209, 213, 650."                              #変数lineに文字列型オブジェクトを保存
m = re.findall("\d", line)                                                             #文字列型オブジェクトlineの中から数値「"\d"」を検索して出力値(戻り値)として変数mに保存
print(m)                                                                               #リスト型オブジェクトmを出力

#問題3
import re                                                                              #re(regualr expression)モジュールをインポート

line = "The ghost that says boo haunts the loo!"                                       #変数lineに文字列型オブジェクトを保存
m = re.findall(".oo", line, re.IGNORECASE)                                              #文字列型オブジェクトlineの中から「o」が０回以上繰り返す文字列を検索して出力値(戻り値)として変数mに保存⇒フラグIGNORECASEで大文字小文字の区別を無視する
print(m)                                                                               #リスト型オブジェクトmを出力