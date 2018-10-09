# _*_ encoding: utf-8 _*_
__author__ = 'guagua'
__date__ = '2018/10/7/007 10:35'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):

    list_display = ['name', 'desc', 'add_time']

    search_fields = ['name', 'desc']

    # course是外键，为了后台过滤器实现外键字段过滤，采用course__name的方式即可，双下划线
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin (object):

    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'city', 'add_time']

    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'city']

    # course是外键，为了后台过滤器实现外键字段过滤，采用course__name的方式即可，双下划线
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'city', 'add_time']


class TeacherAdmin (object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point',
                    'click_nums', 'fav_nums', 'add_time']

    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point', 'click_nums', 'fav_nums']

    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point',
                   'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
