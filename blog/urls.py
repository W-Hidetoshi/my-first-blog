#cording:utf-8
from django.urls import path,re_path,include
from . import views
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('accounts/',include('django.contrib.auth.urls')),
]
