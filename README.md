# [flask](https://flask.pocoo.org) 学习笔记

Flask非常小，一旦你能熟练使用它，很可能就能读懂它所有的源码。

Flask主要有两个依赖：

- 路由，调试和Web服务器网关接口（WSGI）子系统由[Werkzeug](https://werkzeug.pocoo.org/)提供；
- 模版系统由[Jinja2](https://jinja2.pocoo.org/)提供

Flask并不原生支持数据库访问，Web表单验证和用户认证等高级功能。这些功能以都以扩展的形式实现。



## GitHub

`$ git clone https://github.com/miguelgrinberg/flask.git`

`$ git checkout 1a`

`$ git reset --hard`



`$ git fetch --all`

`$ git fetch --tags`

`$ git reset --hard origin/master`



`$ git diff 2a 2b`



## 第1章 安装

### win下安装easy_install

进入:https://bitbucket.org/pypa/stuptools

下载脚本文件，脚本名为ez_setup.py

在脚本文件夹下执行命令：`python ez_install.py`

### win下安装虚拟环境

`easy_install virtualenves`

### win下虚拟环境命令：

创建：`virtualenv venv`

激活： `venv\Scripts\activate`

安装flask：`pip install flask`

运行app：`python hello.py`

结束运行：ctrl+c



查看运行效果： 	

https://localhost:5000 	

https://127.0.0.1:5000





## 第2章 程序的基本结构

### 一个完整的程序

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
	app.run(debug = True)
```

*动态路由*

```python
@app.route('/output/<text>')
def output(text)
	return '%s' % text 	
```



### 请求-响应循环

*客户端发来的请求*



#### 程序和请求上下文

```python
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is </p>' % user_agent
```

| 变量名         | 上下文   | 说明                          |
| ----------- | ----- | --------------------------- |
| current_app | 程序上下文 | 当前激活程序的程序实例                 |
| g           | 程序上下文 | 处理请求时用作临时存储的对象。每次请求都会重设这个变量 |
| request     | 请求上下文 | 请求对象，封装了客户端发出的HTTP请求中的内容    |
| session     | 请求上下文 | 用户会话，用于存储请求之间需要“记住”的值的词典    |

> **使用前必须激活（或推送）** ，什么意思？如何激活？



#### 请求调度

> 每个URL有三个请求方法 `(HEAD,OPTIONS,GET)`  

> `HEAD`,`OPTIONS`由flask自动处理

> 由此可推断上文程序中的路由都**<u>采用</u>**[^?]`GET`方法

??????



#### 请求钩子

- `before_first_request` : 注册一个函数，在处理第一个请求之前运行。
- `before_request` : 注册一个函数，在处理每次请求之前运行。
- `after_request` : 注册一个函数，如果没有未处理的异常，在处理每次请求之后运行。
- `teardown_request` : 注册一个函数，即使有未处理的异常， 也在每次请求之后运行。

#### 响应

##### 返回 1、2或3个参数

1. 字符串
2. 状态码：200 - 请求处理成功 ， 400 - 请求无效
3. 一个由首部(header)组成的字典

```python
@app.route('/')
def index():
    return '<h1>Bad Request</h1>' , 400
```



##### 返回 Response对象

```python
from flask import make_response

@app.route('/')
def index():
    response = make_response('<h1>This document carries a  cookies!</h1>')
    response.set_cookie('answer' , '42')
    return response
```



##### 重定向

```python
from flask import redirect

@app.route('/')
def index():
    return reditect('http://www.example.com')
```



##### 抛出异常

```python
from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello , %s</h1>' % user.name
```





### Flask扩展

#### Flask-Script

```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)

#...

if __name__ == '__main__':
    manager.run()
```



shell		在Flask应用上下文中运行Python shell

runserver	运行Flask 开发服务器： app.run()



`$python hello.py --help`

```
（venv）$ pyhton hello.py runserver --host 0.0.0.0
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```



## 第3章 模版



## 第4章 Web表单



request.form 能获取 POST请求提交的表单数据

更简单的方法：

[Flask-WTF](https://pythonhosted.org/Flask-WTF/)扩展对[WTFrms](https://wtformssimple.com)包进行了包装

`pip install flask-wtf`

 

### 跨站请求伪造保护

```python
app = flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

app.config字典用来存储框架，扩展，程序本身的配置变量。



### 表单类

```python
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('what is your name?', validators = [Required()])
    submit = SubmitField('Submit')
```

 





