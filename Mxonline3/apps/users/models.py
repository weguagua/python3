# encoding: utf-8
from django.db import models
from datetime import datetime


# 用户信息表
class UserProfile(models.Model):
    nick_name = models.CharField(max_length=20, verbose_name='昵称')
    birthday = models.DateTimeField(default=datetime.now, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), verbose_name='性别')
    address = models.CharField(max_length=200, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='电话号码')
    # 图片在库中存储的是图片所在路径
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', verbose_name='头像', max_length=100)

    # 定义表的名字，同时也是后台管理中的菜单名字
    class Meta:
        verbose_name = '用户信息'
        # verbose_name_plural是verbose_name的复数形式
        # 如果不设置，在后台管理中，Django就会在菜单名字后面加上一个s
        verbose_name_plural = verbose_name

        # Django的后台，实际上是对我们新建的每个表做了增删改查的管理


# 邮箱验证码表
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    # 两类情况下发送验证码
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '忘记密码')),
                                 max_length=10, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '验证码管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图表
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图管理'
        verbose_name_plural = verbose_name
