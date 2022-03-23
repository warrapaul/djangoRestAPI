from django.urls import path
from methodBased import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('buildings/', views.building_list),
    path('buildings/<int:pk>/', views.building_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)