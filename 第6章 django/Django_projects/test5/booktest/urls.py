from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^myexp$',views.myExp),
    url(r'^uploadpic$',views.uploadPic),
    url(r'^uploadhandle$',views.uploadhandle),
    url(r'^herolist/(\d+)/$',views.herolist),
    url(r'^area/$',views.area),
    url(r'^area/(\d+)/$',views.area2),
]