# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

#注册的第二种方案:
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date','bread','bcommet']

#注册第一种方案:
#admin.site.register(BookInfo,BookInfoAdmin)
