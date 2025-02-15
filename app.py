from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置 MySQL 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:yourpassword@localhost/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建数据库对象
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(80), unique=True, nullable=False) # 姓名
    email = db.Column(db.String(120), unique=True, nullable=False) # 邮箱

with app.app_context():
    # 创建表
    db.create_all()

@app.route("/")
def home():
    return "Hello, AWS CI/CD updated on Feb 15! 🚀 Now with Auto Deployment! Now Flask is connected to MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
