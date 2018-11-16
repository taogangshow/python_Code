# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache

def index(request):
    return render(request,'booktest/index.html')

def pro(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)
    list = []
    # [[1,'北京'],[2,'河北'],...]
    for item in prolist:
        list.append([item.id,item.title])#[1,'北京']
    return JsonResponse({'data':list})

def city(request,id):
    citylist = AreaInfo.objects.filter(parea_id=id)
    list = []
    #[{id:1,title:'北京'},{id:2,title:'河北'},...]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})#{id:1,title:'北京'}
    return JsonResponse({'data':list})

#自定义编辑器
def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')

def htmlEditorhandle(request):
    html = request.POST['hcontent']
    test1 = tinymceTest1.objects.get(pk=1)
    # 将自定义编辑中的内容赋给django amdin用户的content　
    test1.content = html
    #将数据存到数据库
    test1.save()
    '''
    增加admin的content属性第一种方法
    test1 = tinymceTest1()
    test1.content = html
    test1.save()

    增加admin的content属性第二种方法
    在模型中写个管理器定义create方法
    调用create方法也可以完成增加操作
    '''
    context = {'content':html}
    return render(request,'booktest/htmlShow.html',context)

#缓存
#@cache_page(60*10)
def cache1(request):
    # return HttpResponse('hello1')
    # return HttpResponse('hello2')
    # 需导入from django.core.cache import cache

    # 设置：cache.set(键, 值, 有效时间)
    # 获取：cache.get(键)
    # 删除：cache.delete(键)
    # 清空：cache.clear()
    # cache.set('key1','value1',600)
    # print(cache.get('key1'))
    # return render(request,'booktest/cache1.html')
    cache.clear()
    return HttpResponse('清除缓存完毕!')

#全文检索＋中文分词
def mysearch(request):
    return render(request,'booktest/mysearch.html')

#celery异步处理
def celeryTest(request):
    from task import *
    # show()
    show.delay()
    return HttpResponse('hello world')