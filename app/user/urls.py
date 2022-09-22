"""
User mapping for the user API.
"""
from django.urls import path
from user import views

# reverse of CREATE_USER_URL in test_user_api.py
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserview.as_view(), name='create'),
    pasth('token/', views.CreateTokenview.as_view(), name='toeken'),