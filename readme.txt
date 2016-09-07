readme

8-24
Flask 1 day

虚拟环境 $ virtualenv --version
！！！！！！！！！！！！！！！！！！！！！！！！
	进入python所在的文件夹
	$ pip install virtualenv
！！！！！！！！！！！！！！！！！！！！！！！！

windows激活虚拟机命令
$ venv\Scripts\activate
激活需要在cmd中，进入flasky
回到全局解释器
$ deactivate

！！！！！！！！！！！！！！！！！！！！！！！！
	然后安装flask
	(venv) $ pip install flask
！！！！！！！！！！！！！！！！！！！！！！！！

处理URL和函数之间关系的程序称为路由

8-25
Flask 2 day

tag:1a 的 hello.py 是静态路由 手动改变文件后 想切换到其他 tag 就会被警告 做出选择 commit-提交更改 stash-隐藏更改
Acer@Acer_PC MINGW64 ~/flasky ((1a))
$ git checkout 2b
error: Your local changes to the following files would be overwritten by checkout:
        hello.py
Please, commit your changes or stash them before you can switch branches.
Aborting

选择隐藏 tag 就返回最初
Acer@Acer_PC MINGW64 ~/flasky ((1a))
$ git stash
Saved working directory and index state WIP on (no branch): 7e1e156 Chapter 1: initial version (1a)
HEAD is now at 7e1e156 Chapter 1: initial version (1a)

之后就可以切换 tag 了

9-7
Flask 3 day

app.route修饰器

状态码400-请求无效
状态码302-重定向
状态码404-URL中动态参数id对应的用户不存在

拓展包含在flask.ext命名空间下

书与现有模块使用方法略有差别
现  runserver:
		[-?] --help
		[-h] --host

模板：
	包含响应文本的文件，包含占位变量表示的动态部分

渲染：
	使用真实值替代变量，再返回最终得到的响应字符串

变量过滤器：
	safe		渲染值时不转意
	capitalize	把值的首字母转成大写，其余小写
	lower		把值转换成小写
	upper				  大写
	title		值中每个单词的首字母转成大写
	trim		把值得首尾空格去掉
	striptagd	渲染前删掉HTML标签

Flask-Script (拓展) ,为Flask程序添加一个命令行解析器
Flask-Bootstrap (拓展) ,Twitter开发的开源客户端框架，提供用户界面组件，兼容所有现代Web浏览器
















