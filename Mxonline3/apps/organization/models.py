# encoding: utf-8
from django.db import models
from datetime import datetime


# 城市表
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名')
    desc = models.CharField(max_length=200, verbose_name='城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '所在城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构表
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='封面图', max_length=100)
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教师表
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')

    work_position = models.CharField(max_length=50, verbose_name='职位')
    point = models.CharField(max_length=50, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '授课讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
