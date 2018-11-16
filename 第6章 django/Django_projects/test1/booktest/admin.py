# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *
#from .models import * ----python3
# Register your models here.
#因为admin模块就在booktest下　所以不用写booktest.models

#实现关联注册
class HeroInfoInline(admin.TabularInline): #除了继承admin.TabularInline还可以继承admin.StackedInline
    model = HeroInfo #在添加图书bookinfo时候，额外添加heroinfo这个类,即model=HeroInfo 一对多关系
    extra = 3#额外添加几个数据

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fieldsets = [
        ('basic',{'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']}),
    ]

    inlines = [HeroInfoInline]#指定关联注册类

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
