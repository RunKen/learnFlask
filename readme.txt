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