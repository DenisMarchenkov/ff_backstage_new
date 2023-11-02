from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm


# def login_user(request):
#     # Мы здесь вначале создаем форму LoginUserForm с набором принятых данных request.POST.
#     # Затем, проверяем форму на корректность (валидность) и если проверка проходит,
#     # то создаем временную переменную cd,
#     # которая ссылается на очищенные принятые данные формы.
#     # На основе полей username и password мы пытаемся с помощью функции authenticate()
#     # аутентифицировать пользователя по таблице user БД.
#     # Если пользователь с указанной парой логин/пароль находится в БД и является активным (не забанен, например),
#     # то вызывается ключевая функция login(), которая создает запись в сессии, авторизуя
#     # текущего пользователя на сайте.
#     # После этого делается перенаправление на главную страницу.
#     # В случае каких-либо ошибок снова форма отображается в браузере пользователя,
#     # предлагая ему еще раз попробовать ввести логин и пароль.
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('stock'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('stock:stock')
