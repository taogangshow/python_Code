# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse('hello world')

def detail(request,p1):
    return HttpResponse(p1)

def showdate(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))

def showdate_P(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))

#展示链接的界面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)

#接收一键多值的情况
def getTest3(request):
    a1 = request.GET.getlist('a')
    context = {'a':a1}
    return render(request,'booktest/getTest3.html',context)

#post请求
def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    username = request.POST['username']
    pwd = request.POST['pwd']
    gender = request.POST['gender']
    like = request.POST.getlist('like')
    site = request.POST['site']
    info = request.POST['info']
    context = {'username':username,'pwd':pwd,'gender':gender,'like':like,'site':site,'info':info}
    return render(request,'booktest/postTest2.html',context)

#cookie
def cookieTest(request):
    response = HttpResponse()
    #获取cookie对象
    cookie = request.COOKIES
    #判断这个cookie对象中是否存在t1这个cookie,返回boolean
    if cookie.has_key('t1'):
        response.write('<h1>'+cookie['t1']+'</h1>')

    #response.set_cookie('t1','hello cookie')
    #response.write('<h1>111</h1>')
    return response

#重定向
def redTest1(request):
    #return HttpResponseRedirect('/booktest/redTest2')
    return redirect('/booktest/redTest2')

def redTest2(request):
    return HttpResponse('<h1>这是转向来的页面</h1>')

#session用户登录
def session1(request):
    #uname = request.session['myname']
    uname = request.session.get('myname','未登录')
    context = {'uname':uname}
    return render(request,'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handel(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    #判断用户名和密码是否正确
    if uname == 'taogang' and upwd == '123456':
        #写入session
        request.session['myname']=uname
        #设置session过期时间为关闭浏览器时过期
        request.session.set_expiry(0)
        return redirect('/booktest/session1/')
    elif uname != 'taogang':
        return HttpResponse('用户名不存在...')
    elif uname == 'taogang' and upwd != '123456':
        return HttpResponse('密码错误...')

#删除session完成注销
def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')


