# モジュール

# <組み込み関数>
# モジュール内のプログラム(変数や関数)を使用
import math
math.pow(2, 3) #mathモジュールのpow関数を使用する

import random          #randomモジュールをインポートして使用できるようにする
random.randint(0, 100) #randomモジュールのrandint関数を使用する

import statistics                #statisticsモジュールをインポートして使用できるようにする
nums = [1, 5, 33, 12, 46, 33, 2] #変数numsにリスト型オブジェクトを保存

print(statistics.mean(nums))     #statisticsモジュールのmean関数を使用してリスト型オブジェクトnumsの平均値を計算する
print(statistics.median(nums))   #同上のmedian関数を使用してリスト型オブジェクトnumsの中央値を計算する
print(statistics.mode(nums))     #同上のmode関数を使用してリスト型オブジェクトnumsの最頻値を計算する

import keyword #keywordモジュールをインポートして使用できるようにする

print(keyword.iskeyword("for")) #keywordモジュールのiskeyword関数を使用して文字列型オブジェクトforがPythonのキーワードかどうかを確認する
print(keyword.iskeyword("football")) #同上のiskeyword関数を使用して文字列型オブジェクトfootballがPythonのキーワードかどうかを確認する

# <別のモジュールをインポート>
# 自作モジュールをインポート
import mylib

mylib.print_hello() #mylibモジュールのprint_hello関数を使用する

# 指定したプログラム以外は実行しない
import mylib
mylib.print_hello() #指定したモジュール内のプログラムは実行される

# <チャレンジ>
# 問題1
import statistics

data = [14, 3, 11, 133, 4]
print(statistics.median_low(data)) #statisticsモジュールのmedian_low関数を呼び出して入力値(引数)にリスト型オブジェクトdataを渡す

# 問題2
import mylib #mylibモジュールをインポート

result = mylib.cube_it(5) #mylibモジュールのcube_it関数を呼び出して入力値(引数)に整数型オブジェクト「5」を渡す
print(result)