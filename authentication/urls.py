from django.urls import path
from authentication import views

urlpatterns = [
    path('buildings/', views.building_list.as_view()),
    path('buildings/<int:pk>/', views.building_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDeatil.as_view()),
]
