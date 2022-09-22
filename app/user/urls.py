"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

# reverse of CREATE_USER_URL in test_user_api.py
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    pasth('token/', views.CreateTokenView.as_view(), name='token'),
]