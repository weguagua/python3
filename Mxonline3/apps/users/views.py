# encoding: utf-8

# import json

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# Django自带的用户验证,login
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.backends import ModelBackend

from courses.models import Course
# from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from .models import UserProfile, EmailVerifyRecord, Banner
# 并集运算
# from django.db.models import Q
# 基于类实现需要继承的view
from django.views.generic.base import View
# form表单验证 & 验证码
# from .forms import LoginForm, RegisterForm, ActiveForm, ForgetForm, ModifyPwdForm, UploadImageForm, UserInfoForm
# 进行密码加密
# from django.contrib.auth.hashers import make_password
# 发送邮件
# from utils.email_send import send_register_eamil
#from pure_pagination import Paginator, PageNotAnInteger


# 首页
class IndexView(View):
    def get(self, request):
        # 取出轮播图
        # all_banner = Banner.objects.all().order_by('index')[:5]
        # 正常位课程
        # courses = Course.objects.filter(course_org_id=False)[:6]
        # 轮播图课程取三个
        # banner_courses = Course.objects.filter(course_org_id=True)[:3]
        # 课程机构
        # course_org = CourseOrg.objects.all()[:10]
        return render(request, 'index.html', {})

