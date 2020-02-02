from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new')
]
