from django.urls import path
from classBased import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('buildings/', views.building_list.as_view()),
    path('buildings/<int:pk>/', views.building_detail.as_view()),
]
from rest_framework.urlpatterns import format_suffix_patterns
