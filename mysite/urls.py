
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static # ch10 1/4
from django.conf import settings           # ch10 2/4
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),  # 추가!!!
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^notice/', include('notice.urls', namespace='notice')),
    # notice.urls를 적용하고, 이름공간을 'notice'로 지정
    url(r'^qna/', include('qna.urls', namespace='qna')),
    # qna.urls를 적용하고, 이름공간을 'qna'로 지정
    url(r'^review/', include('review.urls', namespace='review')),
    # review.urls를 적용하고, 이름공간을 'review'로 지정
    # 아래 인증 URL 3개 추가(ch11 추가)
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^photo/', include('photo.urls', namespace='photo')),          # ch10 3/4
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)         # ch10 4/4

