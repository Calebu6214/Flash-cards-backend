from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/subject/$', views.SubjectList.as_view()),
    url(r'api/subject/subject-id/(?P<pk>[0-9]+)/$',views.SubjectDescription.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)