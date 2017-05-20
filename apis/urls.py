from django.conf.urls import url
from apis import views

urlpatterns = [
    url(r'^apis/$', views.snippet_list),
    url(r'^apis/(?P<pk>[0-9]+)/$', views.snippet_detail)
]