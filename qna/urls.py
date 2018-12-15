
from django.conf.urls import url
from qna.views import *
urlpatterns = [

    # Example: /
    url(r'^$', QnALV.as_view(), name='index'),

    # Example: /qna/ (same as /)
    url(r'^qna/$', QnALV.as_view(), name='qna_list'),

    # Example: /qna/django-example/
    url(r'^qna/(?P<slug>[-\w]+)/$', QnADV.as_view(), name='qna_detail'),

    # Example: /archive/
    url(r'^archive/$', QnAAV.as_view(), name='qna_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', QnAYAV.as_view(), name='qna_year_archive'),

    # # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', QnAMAV.as_view(), name='qna_month_archive'),
    # # Example: /2012/11/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostMAV.as_view(), name='post_month_archive'),

    # # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', QnADAV.as_view(), name='qna_day_archive'),
    # # Example: /2012/11/10/
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    url(r'^today/$', QnATAV.as_view(), name='qna_today_archive'),
]
