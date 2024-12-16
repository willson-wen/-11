from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# 基本配置
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 路由配置
@app.route('/')
def index():
    return 'Hello World!'

# 确保有这个处理程序
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page Not Found", 404

# Vercel 需要这个
app = app.wsgi_app if os.getenv('VERCEL_ENV') else app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 