from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

app_name = 'members'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(template_name='registration/change-password.html'), name="password_change"),
    # path('/<int:id>/password/', ChangePasswordView.as_view(template_name='registration/change-password.html'), name="password_change"),
    path('done', password_success, name='done'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile_page/<int:user_id>', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    
    
]