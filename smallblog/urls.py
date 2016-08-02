from django.conf.urls import patterns,include,url
from smallblog import views

urlpatterns = patterns('',
    url(r'^$', views.post_list),
)

