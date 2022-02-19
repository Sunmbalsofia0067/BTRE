from django.urls import path
from accounts import views

urlpatterns = [
    path('contacts', views.inquiry, name='accounts'),
]