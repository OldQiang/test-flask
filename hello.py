#-*- coding:utf-8 -*-

from datetime import datetime
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
bootstrap = Bootstrap(app)
mament = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
	

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/mei')
def mei():
    return render_template('mei.html')

	
@app.route('/sb/<name>')
def sb(name):
    return render_template('sb.html',name=name)

	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug = True)

