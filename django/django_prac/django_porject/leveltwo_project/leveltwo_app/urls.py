from django.urls import path
from leveltwo_app import views

urlpatterns = [
    path('users/', views.user, name = 'users'),
]
