from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^conv/(?P<pk>[0-9]+)/$', views.conv_detail, name='conv_detail'),
]
