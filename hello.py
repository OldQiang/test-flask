#-*- coding:utf-8 -*-

#---- fix UnicodeDecodeError -----
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#---------------------------------

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Grey Wall</h1>'

@app.route('/mei')
def mei():
    return '<h1>小湄天仙</h1>'

	
@app.route('/sb/<name>')
def sb(name):
    return '<h1>%s 是 傻逼！<h1>' % name
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug = True)

