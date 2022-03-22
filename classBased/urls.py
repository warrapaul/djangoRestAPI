from django.urls import path
from classBased import views

urlpatterns = [
    path('buildings/', views.building_list.as_view()),
    path('buildings/<int:pk>/', views.building_detail.as_view()),
]
