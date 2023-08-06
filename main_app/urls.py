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
    path('builders/<int:builder_id>/assoc_contractor/<int:contractor_id>/', views.assoc_contractor, name='assoc_contractor'),
    path('builders/<int:builder_id>/unassoc_contractor/<int:contractor_id>/', views.unassoc_contractor, name='unassoc_contractor'),
    path('contractors/', views.ContractorList.as_view(), name='contractors_index'),
    path('contractors/<int:pk>/', views.ContractorDetail.as_view(), name='contractors_detail'),
    path('contractors/create/', views.ContractorCreate.as_view(), name='contractors_create'),
    path('contractors/<int:pk>/update/', views.ContractorUpdate.as_view(), name='contractors_update'),
    path('contractors/<int:pk>/delete/', views.ContractorDelete.as_view(), name='contractors_delete'),
    ]

