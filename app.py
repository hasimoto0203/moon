from flask import Flask, render_template

# Flaskのアプリを立ち上げる準備
app = Flask(__name__, template_folder='.')

# ユーザーがサイト（トップページ）にアクセスしたときの処理
@app.route('/')
def home():
    # さっき作った index.html を画面に表示する
    return render_template('index.html')

# プログラムを起動する設定
if __name__ == '__main__':
    app.run(debug=True)