#-*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>home page</h1>'

@app.route('/mei')
def mei():
    return '<h1>小湄天仙</h1>'

@app.route('/print/<string>')
def output(string):
    return '<h2>%s</h2>' %string

if __name__ == '__main__':
	app.run(debug = True)

