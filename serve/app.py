from flask import Flask,render_template

import pymysql

try:
    db = pymysql.connect(host='localhost', user='root', passwd='666666', port=3306)
    print('连接成功！')
except:
    print('something wrong!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('/temp/index.html')