from django.urls import path
from members.views import UserRegister, UserEdit, password_success, PasswordChange
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit-profile'),
    path('password/',PasswordChange.as_view(), name='change-password'),
    path('password_success/', password_success, name='password-change-success'),
]