# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect
import time

website = Flask(__name__)

@website.route('/')
def index():
    return render_template('index.html')                #起点


@website.route('/login',methods=['GET','POST'])        #登录
def login():
    if request.method == "GET":                         #判断请求为什么格式，get就跳转的登录页面，post就判断是否已经注册，已经注册就跳转到登录后页面
        return render_template('login.html')
    elif request.method == "POST":
        f =request.form.to_dict()                       #f是这次post请求的详细信息，储存为字典格式
        info = open('login-info.txt','a',encoding='utf-8')  #此处将post请求的详细情况记录下来
        info.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
        info.write(str(f))
        info.write("\n-------------------\n")
        info.close()
        cunzai = 0
        zh = request.form.get("zh")
        mm = request.form.get("mm")
        fp = open("User.txt",'r',encoding='utf-8')      #此处判断是否已经注册
        for line in fp:
            if zh + " " + mm == line.strip():
                cunzai = 1
        if cunzai == 1:                                 #如果已经注册，进行重定向，传递的参数为用户名
            return redirect(url_for("hello_name",name = zh),code=302)
        elif cunzai == 0:                               #如果没有注册，返回这个
            return "你还没注册呢"
    else:
        return '404'


@website.route('/register/',methods=['GET','POST'])     #注册
def register():
    if request.method == "GET":                         #判断请求格式，如果是get就返回注册页面，如果是post就返回注册成功页面
        return render_template('register.html')
    elif request.method == "POST":
        f = request.form.to_dict()                      #此处将这次post的详细信息储存下来
        info = open('register-info.txt','a',encoding='utf-8')
        info.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
        info.write(str(f))
        info.write("\n-------------------\n")
        info.close()
        zh = request.form.get("zh")
        mm = request.form.get("mm")
        s = "账号 " + zh + " 注册成功"
        fp = open("User.txt",'a',encoding='utf-8')
        fp.write(zh + " " + mm + "\n")
        fp.close()
        return s                                        #返回注册成功的信息
    else:
        return "404"


@website.route('/hello')            #路由
def hello_world():
    return "hello"


@website.route('/?<string:name>')   #变量规则
def hello_name(name):
    return 'hello %s!' %name


if __name__ == "__main__":
    website.run(host='0.0.0.0',port=5000,debug=True)    #默认端口号为5000
