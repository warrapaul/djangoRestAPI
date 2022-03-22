from django.urls import path
from methodBased import views

urlpatterns = [
    path('buildings/', views.building_list),
    path('buildings/<int:pk>/', views.building_detail),
]
