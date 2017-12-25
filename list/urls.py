from django.conf.urls import url
from . import views

app_name = 'list'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="restaurantList"),
    url(r'^(?P<pk>[0-9]+)/$', views.MenuListView.as_view(), name="menuList"),
]
