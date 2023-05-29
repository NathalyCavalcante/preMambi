from django.shortcuts import render, redirect
from worker.models import Professions, Member # importa do app worker os modelos para serem exibidos, renderizados
from .forms import SignupForm # importa o form de login que criamos
from django.contrib.auth import logout

# página inicial
def index(request):
    member = Member.objects.all()
    professions = Professions.objects.all()
    # precisa depois de criar as variáveis acima, um dicionário abaixo
    return render(request, 'core/index.html', {
        'member': member,
        'professions': professions,
    })

# página de contato
def contact(request):
    return render(request, 'core/contact.html')

# assinar
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
        
    })

def logoff(request):
    logout(request)
    return redirect('/login/')
