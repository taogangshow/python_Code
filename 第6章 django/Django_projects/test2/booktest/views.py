# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import *
from django.db.models import Max,F,Q
# Create your views here.
def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    max_num = BookInfo.books1.aggregate(Max('bpub_date'))
    list2 = BookInfo.books1.filter(bread__gt=20)
    list3 = BookInfo.books1.filter(bread__gt=F('bcommet'))
    list4 = BookInfo.books1.filter(Q(pk__lt=6) | Q(btitle__contains='1'))
    context={'list':list,'max_num':max_num,'list2':list2,'list3':list3} 
    return render(request,'booktest/index.html',context)
