from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    url(r'^lists/new$', views.new_list, name='new_list'),
]