from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from stock.utils import MenuMixin
from users.forms import LoginUserForm


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class LoginUser(MenuMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('stock:stock')
