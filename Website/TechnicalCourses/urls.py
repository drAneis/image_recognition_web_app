from django.urls import  path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [


    path('', views.Courses, name='home-page'),
    path('uploadpage', views.upload_photo, name='detail'),
    path('upvideo', views.upload_video, name='video'),


]


# only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
