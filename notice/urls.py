"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from notice.views import * # 이렇게 수정하면 아래와 같이 views.~ 형식에서 views. 부분을 빼야 함
                         # bookmark.urls에서는 from . import views로 했으므로 views.~ 형식으로 사용해야 함
#  아래에서 blog/ 부분은 이미 처리되고 넘어온 상황임

urlpatterns = [

    # Example: /
    url(r'^$', NoticeLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    url(r'^notice_post/$', NoticeLV.as_view(), name='notice_list'),

    # Example: /post/django-example/
    url(r'^notice_post/(?P<slug>[-\w]+)/$', NoticeDV.as_view(), name='notice_detail'),

    # Example: /archive/
    url(r'^notice_archive/$', NoticeAV.as_view(), name='notice_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', NoticeYAV.as_view(), name='notice_year_archive'),

    # # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', NoticeMAV.as_view(), name='notice_month_archive'),
    # # Example: /2012/11/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostMAV.as_view(), name='post_month_archive'),

    # # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', NoticeDAV.as_view(), name='notice_day_archive'),
    # # Example: /2012/11/10/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    url(r'^today/$', NoticeTAV.as_view(), name='notice_today_archive'),
]
# 위에서 지정한 name 항목을 템플릿에서 사용할 때에는 이름공간을 포함하여,
# blog:index, blog:post_list, blog:post_detail, blog:post_archive, ... 로 명시해야 함
