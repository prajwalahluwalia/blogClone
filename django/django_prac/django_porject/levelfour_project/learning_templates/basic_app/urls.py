from django.urls import path, include
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_template, name='relative'),
    path('other/', views.other, name='other'),
]