# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    # null = True　可以为空,　blank=True 在页面表单添加内容可以不填
    parea = models.ForeignKey('self',null=True,blank=True)

class tinymceTest1(models.Model):
    content = HTMLField()

