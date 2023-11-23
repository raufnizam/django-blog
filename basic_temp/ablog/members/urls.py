from django.urls import path
from .views import UserRegisterView, UserEditView, password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Use Django's built-in LoginView
    path('logout/', LogoutView.as_view(), name='logout'),  # Optional: Add a logout view
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html'), name="password_change"),
    path('password/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('done/', password_success, name='done'),
]
