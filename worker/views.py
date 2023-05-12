from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect # importa o get object
from .models import Member # importar o model que precisamos das informações
from .forms import NewMemberForm

# Create your views here.

def profile(request, pk): 
    # primary key que fizemos no model do worker app
    worker= get_object_or_404(Member, pk=pk) 
    # pegar do model Member, e pk do model e pk da url
    related_worker = Member.objects.filter(profession=worker.profession).exclude(pk=pk) [0:3]
    # para exibir demais com a mesma profissão e excluir o que está sendo exibido, não entendi o [0:3] mas só funciona com ele.

    return render(request, 'worker/profile.html', { 
        # 'member/profile.html' me manda criar um novo folder 'member' e novo template 'profile' dentro do woeker
        'worker': worker,
        'related_worker': related_worker
    })
# segue para criação do template e criação da url (cria os arquivos)

# preciso que o django requeira que o usuário esteja logado para acessar essa view, por isso a importação lá em cima
@login_required # decorator importado
def new(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST, request.FILES)
        # COLOQUEI MEMBER MAS PODE SER QUE SEJA WORKER
        if form.is_valid():
            member = form.save(commit=False) # perfil criado por 'field' não vai ser adicionado no database
            member.created_by = request.user # perfil criado por 'usuário autenticado no login' salva no database
            form.save()

            return redirect('worker:profile', pk=member.id)
    else:
        form = NewMemberForm()

    return render(request, 'worker/form.html', {
        'form': form,
        'title': 'New member'
    })


@login_required
def delete(request, pk): # pk é por causa da id do member que quer deletar
    member = get_object_or_404(Member, pk=pk, created_by=request.user)
    member.delete()

    return redirect('dashboard:index')