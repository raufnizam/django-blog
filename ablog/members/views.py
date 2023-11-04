from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, ProfilePageForm
from django.http import Http404
from django.contrib.auth.models import User
from theblog.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        user_id = self.kwargs['user_id']  # Get the user_id from URL parameters
        if Profile.objects.filter(user_id=user_id).exists():
            # If a profile already exists for the user, redirect to the edit profile page
            return redirect(reverse_lazy('members:edit_profile_page', kwargs={'user_id': user_id}))

        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user_id = self.kwargs['user_id']  # Get the user_id from URL parameters
        form.instance.user = User.objects.get(pk=user_id)
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url']
    success_url = reverse_lazy('members:show_profile_page')

    
    
    
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user
        return context



class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm  
    success_url = reverse_lazy('done')


def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_settings.html"
    success_url = reverse_lazy('blog:home')
    
    def get_object(self):
        return self.request.user
