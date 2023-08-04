from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('builders/', views.builders_index, name='index'),
    path('builders/<int:builder_id>/', views.builders_detail, name='detail'),
    path('builders/create/', views.BuilderCreate.as_view(), name='builders_create'),
    path('builders/<int:pk>/update/', views.BuilderUpdate.as_view(), name='builders_update'),
    path('builders/<int:pk>/delete/', views.BuilderDelete.as_view(), name='builders_delete'),
    path('builders/<int:builder_id>/add_propertydetails/', views.add_propertydetails, name='add_propertydetails'),
]

