from unicodedata import name
from flask import Flask
from flask import escape, url_for
app = Flask(__name__)

# set FLASK_APP = hello.py 启动哪个程序
# set FLASK_ENV 用来设置程序运行的环境 production, development

@app.route('/hello') #注册一个处理函数 绑定对应URL
@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    #return "Welcome!!"
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('user_page', name='peter')) # endpoint. set name
    print(url_for('test_url_for'))
    return 'Test'