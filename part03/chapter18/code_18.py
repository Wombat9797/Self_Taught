# パッケージ管理

# <pip>
# Flaskモジュールをインポート
from flask import Flask

app = Flask(__name__)                                                                       #変数appにFlaskメソッドの出力値(戻り値)を保存

@app.route("/")
def index():
    return "Hello, World!"

app.run(port=8000)