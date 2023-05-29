# CRIADO PARA CONCENTRAR TODOS AS PATHS AQUI E NÃO NOS APPS SECUNDÁRIOS PARA DEIXAR MAIS LIMPO
from django.contrib.auth import views as auth_views # para a página log in e não dar crash com o views de baixo já importado
from django.urls import path
from . import views 
# importando todas as views desse app
from .forms import LoginForm
# importando de todos os forms da pasta o Loginform

app_name = 'core'
# criado para facilitar o entendimento

urlpatterns = [
    path('', views.index, name='index'),
    # feita originalmente na urls.py do premambi
    path('contact/', views.contact, name='contact'), 
    path('signup/', views.signup, name='signup'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'), 
    # diferente pq quem vai gerar esse login é o próprio django (e aviso a ele o nome da template)
    # depois desse passo, o django cria uma url de /accounts/profile/ e precisa ir nos settings arrumar
    path('logoff/', views.logoff, name='logoff'), 

]