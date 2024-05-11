# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库连接URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/123?charset=utf8'
# 关闭SQLAlchemy事件追踪，提高性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 直接实例化sqlalchemy对象，传⼊app
db = SQLAlchemy(app)
#将Flask实例对象传入Manager
# manager = Manager(app)
#定义模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

new_user = User(username='john_doe', email='john.doe@example.com')
db.session.add(new_user)
db.session.commit() 