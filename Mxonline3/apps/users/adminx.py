# encoding: utf-8
__author__ = 'guagua'
__date__ = '2018/10/7/007 9:44'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    # 使用主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 页面页头设置
    site_title = '瓜瓜在线后台管理系统'
    # 页脚设置
    site_footer = '瓜瓜在线网'
    # 设置后台主菜单默认收起
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    # 设置后台邮箱验证码列表显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 设置后台邮箱验证码列表搜索可匹配字段
    search_fields = ['code', 'email', 'send_type']
    # 设置后台邮箱验证码列表过滤器--快速搜索
    # 搜索条件的选择方式，由Django根据我们models中的字段类型，自动生成
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 设置后台邮箱验证码列表显示字段
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 设置后台邮箱验证码列表搜索可匹配字段
    search_fields = ['title', 'image', 'url', 'index']
    # 设置后台邮箱验证码列表过滤器--快速搜索
    # 搜索条件的选择方式，由Django根据我们models中的字段类型，自动生成
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
