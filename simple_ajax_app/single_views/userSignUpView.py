from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class UserSignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
