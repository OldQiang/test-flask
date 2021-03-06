#-*- coding:utf-8 -*-

from datetime import datetime
from flask import Flask,render_template,session,url_for,redirect,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = '898934'
app.config['SEVER_NAME'] = 'greywall.dev:80'
bootstrap = Bootstrap(app)
mament = Moment(app)

class NameForm(Form):
	name = StringField("what's your name?", validators = [Required()])
	submit = SubmitField('Submit')
	

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
	

@app.route('/', methods = ['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		new_name = form.name.data
		if new_name == 'mei angel':
			flash('LOVE U *^ 3 ^*')
			flash('LOVE U *^ 3 ^*')
			flash('LOVE U *^ 3 ^*')
			flash('LOVE U *^ 3 ^*')
		elif old_name is not None and old_name != new_name:
			flash('Hello %s !' % new_name)
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/mei')
def mei():
    return render_template('mei.html')


@app.route('/labhtml')
def labhtml():
    return render_template('labhtml.html')

	
@app.route('/sb/<name>')
def sb(name):
    return render_template('sb.html',name=name)

	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug = True)
	
