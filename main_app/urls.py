from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
     path('builders/', views.builders_index, name='index'),
     path('builders/<int:builder_id>/', views.builders_detail, name='detail'),
]

