from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.files_list),
	url(r'^file/(?P<pk>[0-9]+)/$', views.file_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.file_edit, name='post_edit'),
]