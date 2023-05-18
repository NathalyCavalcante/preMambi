from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect # importa o get object
from .models import Member, Professions # importar o model que precisamos das informações
from .forms import NewMemberForm, EditMemberForm
from django.db.models import Q # para poder fazer busca em multiplos campos

# Create your views here.

def browser(request):
    query = request.GET.get('query', '')
    professions = Professions.objects.all()
    profession_id = request.GET.get('professions', 0) # para gerar id
    # poderia ter posto objects.all() para Member mas só descobri isso depois.
    browser = Member.objects.filter(available=True) 

    if query:
        # busca só no nome do worker e não tiver o Q (não consegui colocar a profissão por causa da pk)
        browser = browser.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if  len(browser) == 0:        
            return render(request, 'worker/no_results.html')
    
    if profession_id:
        browser = browser.filter(profession_id=profession_id)

    # palavras para contexto para as variaveis funcionarem na template
    return render(request, 'worker/browser.html', {
        'browser': browser,
        'query': query,
        'professions': professions,
        'profession_id': int(profession_id)        
    })

def no_results(request):
    return render(request, 'worker/no_results.html')


def profile(request, pk): 
    # primary key que fizemos no model do worker app
    worker= get_object_or_404(Member, pk=pk) 
    # pegar do model Member, e pk do model e pk da url
    related_worker = Member.objects.filter(profession=worker.profession).exclude(pk=pk) [0:3]
    # para exibir demais com a mesma profissão e excluir o que está sendo exibido, não entendi o [0:3] mas só funciona com ele.

    return render(request, 'worker/profile.html', { 
        # 'member/profile.html' me manda criar um novo folder 'member' e novo template 'profile' dentro do woeker
        'worker': worker,
        'related_worker': related_worker,
    })
# segue para criação do template e criação da url (cria os arquivos)


# NOVO MEMBRO

# preciso que o django requeira que o usuário esteja logado para acessar essa view, por isso a importação lá em cima
@login_required # decorator importado
def new(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST, request.FILES)
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

# DELETA MEMBRO

@login_required
def delete(request, pk): # pk é por causa da id do member que quer deletar
    member = get_object_or_404(Member, pk=pk, created_by=request.user)
    member.delete()

    return redirect('dashboard:index')


# EDITA MEMBRO

@login_required 
def edit(request, pk):
    member = get_object_or_404(Member, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditMemberForm(request.POST, request.FILES, instance=member) # avisando ao django para editar o que já existe e não um form em branco
        if form.is_valid():
            form.save()

            return redirect('worker:profile', pk=member.id)
    else:
        form = EditMemberForm(instance=member) # avisando ao django para editar o que já existe e não um form em branco

    return render(request, 'worker/form.html', {
        'form': form,
        'title': 'Edit member'
    })

# depois de criar a view do edit, atualiza o url e coloca a nova url no template de profile