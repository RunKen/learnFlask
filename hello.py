from flask import Flask, render_template, session, redirect, url_for, flash
'''	
	render_template-渲染模板	
	session-请求上下文中的变量(用户会话) 
	redirect-重定向,服务器为浏览器POST请求的响应内容为URL,浏览器接收到url后再向服务器发出GET请求,可以防止刷新页面时发出的警告
	url_for-生成url，保证URL和定义的路由兼容，并且修改路由名字后依然可用
	flash-flask核心功能,发给客户端的下一个响应中显示一个消息
'''
from flask_script import Manager
	#添加命令行解析器

from flask_bootstrap import Bootstrap
	#提供用户界面组件，兼容所有现代Web浏览器

from flask_moment import Moment
	#在浏览器中渲染日期和时间

from flask_wtf import Form
	#处理Web表单

from wtforms import StringField, SubmitField
	

from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    manager.run()
