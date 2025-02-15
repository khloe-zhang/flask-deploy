from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置 MySQL 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:yourpassword@localhost/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建数据库对象
db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Hello, AWS CI/CD updated on Feb 15! 🚀 Now with Auto Deployment! Now Flask is connected to MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
