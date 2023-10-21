from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, password_success
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(template_name='registration/change-password.html'), name="password_change"),
    # path('/<int:id>/password/', ChangePasswordView.as_view(template_name='registration/change-password.html'), name="password_change"),
    path('done', password_success, name='done'),
    
    
]