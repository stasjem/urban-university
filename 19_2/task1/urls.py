from django.urls import path

from task1 import views

urlpatterns = [
    # path('', homepageview, name='home')
    path('', views.index),
    path('index1/', views.index1),
]