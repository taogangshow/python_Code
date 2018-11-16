# -*- coding:utf-8 -*-
from django.shortcuts import render
#所有通过浏览器请求过来的报文都不需要我们去构造，Django已经构造好了，但是返回response对象需要我们构造
from django.http import *  #request,response
#导入django模块
#from django.template import RequestContext,loader
# Create your views here.
from .models import *

def index(request):
    #return HttpResponse('hello world')
    
    #temp = loader.get_template('booktest/index.html')#加载templates/booktest/index.html模板
    #return HttpResponse(temp.render())#并将这个模板的内容拿给HttpResponse对象返回给浏览器
    
    #context = {'title':'我的第一个django传输数据'}
    #return render(request,'booktest/index.html',context)
    
    bookList = BookInfo.objects.all()
    context = {'list':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list':herolist}
    return render(request,'booktest/show.html',context)
