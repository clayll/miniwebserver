from django.db import models

# Create your models here.
#定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column="title")#图书名称
    bpub_date = models.DateField(auto_now_add=True, db_column="pub_date")#发布日期
    bread = models.IntegerField(default=0, db_column="read")#阅读量
    bcomment = models.IntegerField(default=0, db_column = "comment")#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除


#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200, null=True, blank=True)#英雄描述信息
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中