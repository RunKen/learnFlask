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
	#StringField-文本字段
    #SubmitField-表单提交按钮

from wtforms.validators import Required
    #验证响应

app = Flask(__name__)
    #__name__-程序主模块,app-程序实例
app.config['SECRET_KEY'] = 'hard to guess string'
'''
    实现CSRF(跨站请求伪造)保护
    使用密钥生成加密令牌，用加密令牌验证请求中表单数据的真伪
    app.config字典可用来储存框架、拓展和程序本身的配置变量
    SECRET_KEY配置变量是通用密钥
'''

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
'''
    name-表单,文本字段
    submit-按钮
    StringField类表示属性为 type="text"的<input>元素
    SubmitField类表示属性为 type="submit"的<input>元素
    字段构造函数的第一个参数是把表单渲染成HTML时使用的标号
    参数validators指定一个由验证函数组成的列表
    验证函数Required()确保提交的字段不为空
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST']) #methods参数告诉Flask在URL映射中把这个视图函数注册为GET和POST请求的处理程序
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') # 直接从会话中读取name参数的值
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data #session['name'] 用户会话,存储用户在表单中输入的名字，两次请求(POST->URL->GET)之间也能记住输入的值
        return redirect(url_for('index')) # redirect辅助函数,生成HTTP重定向响应
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    manager.run()
