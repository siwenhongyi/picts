from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class User(models.Model):
    """
    用户id 昵称 密码 头像 城市 职业 注册时间 最后登录
    """
    user_id = models.CharField(max_length=20, primary_key=True)
    nick_name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    portrait = models.ImageField("portrait", upload_to="picts\\portrait", blank=False, null=False)
    city = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    sign_time = models.DateTimeField('注册时间', default=timezone.now)
    last_time = models.DateTimeField("最后登陆时间", auto_now=True)


class Kind(models.Model):
    """ 类型名称 """
    kind_name = models.CharField(max_length=30, unique=True)


class Pict(models.Model):
    """ 图片id 喜爱数目 类型 上传时间 """
    pict_id = models.CharField(max_length=30, primary_key=True)
    love_num = models.CharField(max_length=30)
    pic_url = models.ImageField(upload_to="background/", blank=False, null=False, default="66")
    kind = models.ManyToManyField(Kind, related_name="pict_kind")
    uploader_time = models.DateTimeField("上传时间", auto_now=True)


class Collection(models.Model):
    """
    用户id-图片id
    收藏时间
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pict_id = models.ForeignKey(Pict, on_delete=models.CASCADE)
    collect_date = models.DateTimeField("收藏时间", auto_now=True)


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.jpg')
