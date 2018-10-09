# _*_ encoding: utf-8 _*_

from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    # 定义后台主菜单中文显示名字
    verbose_name = '课程管理'
