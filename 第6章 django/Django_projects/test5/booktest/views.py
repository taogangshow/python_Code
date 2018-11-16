# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def myExp(request):
    a = int('abc')
    return HttpResponse('hello')

def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

#上传文件并读写到本地
def uploadhandle(request):
    import os
    from django.conf import settings
    pic1 = request.FILES['pic1']
    # picname=/home/python/Desktop/Django_projects/test5/static/media/a1.jpg
    #MEDIA_ROOT = /home/python/Desktop/Django_projects/test5/media
    #pic1.name = a1.jpg
    picname = os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picname,'w') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s">'%pic1.name)

#进行分页练习
def herolist(request,index):
    if index=='':
        index = '1'
    list = HeroInfo.objects.all()
    from django.core.paginator import *
    paginator = Paginator(list,5)
    page = paginator.page(int(index))
    context = {'page':page}
    return render(request,'booktest/herolist.html',context)

#省市区选择
def area(request):
    return render(request,'booktest/area.html')

def area2(request,id):
    id = int(id)
    if id == 0:
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        pass
    # print(data)
    '''
    data对象的内容
    [ < AreaInfo: AreaInfo
    object >, < AreaInfo: AreaInfo
    .........
    object >, < AreaInfo: AreaInfo
    object >, '...(remaining elements truncated)...']
    '''
    list = []
    for area in data:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})#构造出来的json内容{data:[[],[],[]]}
# {"data": [[110000, "\u5317\u4eac\u5e02"],
#中间省略
# [990000, "\u65b0\u7586\u5efa\u8bbe\u5175\u56e2"]]}

