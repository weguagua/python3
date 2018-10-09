# _*_ encoding: utf-8 _*_
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 定义后台主菜单中文显示名字
    verbose_name = '用户信息'
