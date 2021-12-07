#FlaskとプラグインのSQLAlchemyを生成します。
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views

#app.config.from_envvar: 環境変数から読み込む
# app.config.from_object: pythonオブジェクトから読み込む
# app.config.from_pyfile: pythonファイルから読み込む