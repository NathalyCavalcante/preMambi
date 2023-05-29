from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from worker.models import Member
from .models import ConversationArea
from .forms import ConversationMessageForm

# Create your views here.

@login_required
def new_conversation(request, worker_pk):
    worker = get_object_or_404(Member, pk=worker_pk)

    # se vc tenta conversar consigo mesmo
    if worker.created_by == request.user:
        return redirect('dashboad:index')
    # mas vc quer ver todas as conversas suas.
    # o código pega o resultado em comum de todas as conversas entre o worker e o usuário
    conversations = ConversationArea.objects.filter(worker=worker).filter(members__in=[request.user.id])

    # checar se já teve conversa entre o usuário e o worker e o redirecionar para esta conversa
    if conversations:
        # redireciona para a conversa (CÓDIGO FEITO LÁ NA FRENTE EM DEF DETAIL)
        return redirect('conversation:detail', pk=conversations.first().id)

    # checar se a mensagem escrita no form foi enviada no método POST
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # se todo o preenchimento do campo foi feito corretamento, então cria-se a conversação.
            conversation = ConversationArea.objects.create(worker=worker)
            # agora cria-se as pessoas da mensagem
            conversation.members.add(request.user)
            conversation.members.add(worker.created_by)
            # salva a conversa
            conversation.save()

            # commit false para n]ao dá erro no database
            conversation_message = form.save(commit=False)
            # puta que pariu endoidei nessa que não entendi
            conversation_message.conversation = conversation
            # quem criou a mensagem
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('worker:profile', pk=worker_pk)
    else:
        # oferece um form vazio
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })
    
@login_required
def inbox(request):
    # aqui reuniremos todas as conversas que tiveram
    conversations = ConversationArea.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = ConversationArea.objects.filter(members__in=[request.user.id]).get(pk=pk)

    # depois que faz o form de mensagem/send no html, faz a view dele aqui nesse IF
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            # SEM O HTML!!
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    # adiciona o form ao dicionário
    return render(request, 'conversation/detail.html', {
        'form': form,
        'conversation': conversation,
    })


# CRIA AS URLS 
