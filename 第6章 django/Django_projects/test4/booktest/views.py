# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=1)
    list1 = HeroInfo.objects.filter(isDelete=False)
    context = {'hero':hero,'list1':list1}
    return render(request,'booktest/index.html',context)
def show(request,id,id2):
    context = {'id':id,'id2':id2}
    return render(request,'booktest/show.html',context)
#用于练习模板的继承
def index2(request):
    return render(request,'booktest/index2.html')

#测试user1继承于base_user继承于base页面是否成功现实三层继承效果
def user1(request):
    context = {'uname':'jack'}
    return render(request,'booktest/user1.html',context)

def user2(request):
    return render(request,'booktest/user2.html')

#html转义
def htmlTest(request):
    context = {'t1':'<h1>123</h1>',
               't2':'<h1>456</h1>',
               't3':'<div style="color:red;">789</div>'
               }
    return render(request,'booktest/htmlTest.html',context)

#csrf 跨站请求伪造
def csrf1(request):
    return render(request,'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

#验证码
def verifyCode(request):
    # 引入绘图模块
    from PIL import Image,ImageDraw,ImageFont
    import random
    #创建背景色
    bgcolor = (random.randrange(50,100),random.randrange(50,100),0)
    #规定图片宽高
    width=100
    height = 25
    #创建画布
    image = Image.new('RGB',(width,height),bgcolor)
    #构建字体对象
    font = ImageFont.truetype('FreeSansBoldOblique.ttf',24)
    #创建画笔
    draw = ImageDraw.Draw(image)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 干扰线颜色
    def draw_line():
        linecolor = (random.randrange(0,255), random.randrange(0,255), 0)
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=linecolor)
    #创建文本内容
    text = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 逐个绘制字符
    textTemp = ''
    for i in range(4):#一次取6个数
        # 从text文本随即取１个数存在textTemp1变量中
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp+=textTemp1
        # draw.text((0, 0), text, (255, 255, 255), font)
        draw.text((i*25,0),textTemp1,(255,255,255),font)
        draw_line()
    # 将随即生成的6位数存在服务端session中
    request.session['code'] = textTemp
    #将生存的验证码以png格式保存到内存流中
    import cStringIO
    buf = cStringIO.StringIO()
    image.save(buf,'png')
    # 将内存流中的内容输出到客户端
    return HttpResponse(buf.getvalue(),'image/png')

#定义视图测试验证码登陆是否成功
def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')

def verifyTest2(request):
    code1 = request.POST['code1']
    code = request.session['code']
    if code1.upper() == code:
        return HttpResponse('验证成功...')
    else:
        return HttpResponse('验证失败...')
