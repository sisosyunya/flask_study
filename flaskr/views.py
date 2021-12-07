from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


# request:	HTTPリクエストオブジェクト methodやフォームデータにアクセスできる
# render_template:
#  	指定したHTMLテンプレートを使ってレスポンスを返す。
# redirect:	指定したURLにリダイレクトするレスポンスを返す。
# url_for:	指定したエンドポイントに対するURLを返す。
# abort:	指定したHTTPステータスコードのエラーを返す。
# flash:	メッセージを通知するための仕組み