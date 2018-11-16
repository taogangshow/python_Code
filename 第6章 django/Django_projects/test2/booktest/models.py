# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    #重写Manager中的get_queryset方法,返回自己想要的数据
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
    


class BookInfo(models.Model):
    #CharField(max_length=字符长度):字符串，默认的表单样式是 TextInput
    btitle = models.CharField(max_length=20)
    #DateTimeField:使用Python的datetime.datetime实例表示的日期和时间
    bpub_date = models.DateTimeField(db_column='pub_date')
    #IntegerField:整数
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    #BooleanField:true/false 字段，此字段的默认表单控制是CheckboxInput
    isDelete = models.BooleanField(default=False)
    #在模型类中定义类Meta，用于设置元信息
    class Meta:
        #设置数据库表名为bookinfo
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    #ForeignKey：一对多，将字段定义在多的端中
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname
