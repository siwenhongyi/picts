from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class User (models.Model):
    user_id = models.CharField(max_length =10, primary_key=True)
    nick_name = models.CharField(max_length =20)
    password = models.CharField(max_length=30)
    portrait = models.Imagefield("portrait",upload_to ="picts\portrait",blank = False, null = False)
    city = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    sign_time = models.DateTimeField('注册时间',default = timezone.now)
    last_time = models.DateTimeField("最后登陆时间",auto_now = True)

class Pict (models.Model):
    pict_id =models.CharField(max_length=10,primary_key=True)
    love_num =models.CharField(max_length=30)
    kind =models.CharField(max_length=10)
    uploader_time = models.DateTimeField("上传时间",auto_now = True)

class Kind (models.Model):
    kind_name = models.CharField(max_length=30,unique=True)

class Collection (models.Model):
    user_id = models.ForeignKey(User)
    pict_id = models.ForeignKey(Pict)
    collect_date= models.DateTimeField("收藏时间",auto_now = True)



