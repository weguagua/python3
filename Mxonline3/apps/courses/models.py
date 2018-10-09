# encoding: utf-8
from django.db import models
from datetime import datetime


# 课程表
class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    # 富文本存储
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('cf', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name='难度')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节表
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程名称')
    name = models.CharField(max_length=100, verbose_name='章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频表
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节名称')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程资源表
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程名称')
    name = models.CharField(max_length=100, verbose_name='资源名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件', max_length=100)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
