# _*_ encoding: utf-8 _*_
__author__ = 'guagua'
__date__ = '2018/10/7/007 10:18'

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):

    list_display = ['name', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']

    search_fields = ['name', 'degree', 'learn_times', 'students', 'fav_nums',
                     'click_nums']

    list_filter = ['name', 'degree', 'learn_times', 'students', 'fav_nums',
                   'click_nums', 'add_time']


class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time']

    search_fields = ['course', 'name']

    # course是外键，为了后台过滤器实现外键字段过滤，采用course__name的方式即可，双下划线
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin (object):
    list_display = ['lesson', 'name', 'add_time']

    search_fields = ['lesson', 'name']

    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin (object):
    list_display = ['course', 'name', 'add_time', 'download']

    search_fields = ['course', 'name', 'download']

    list_filter = ['course__name', 'name', 'add_time', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
