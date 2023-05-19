from django.db import models
from worker.models import Member # participante do chat
from django.contrib.auth.models import User # participante do chat

# Create your models here.

class ConversationArea(models.Model):

    # aqui cada trabalhador vai ser um que tenha uma FK lá no meu models Member, e o que se vai referir a ele são as 
    # 'conversações' e se deletar um trabalhador, também deleta as conversas dele. Ou seja, conversações do worker.
    worker = models.ForeignKey(Member, related_name='conversations', on_delete=models.CASCADE)
    # quem são os membros das conversas, precisa de multiplos usuários. Será o usuário e o outro "worker", no caso
    # o related_name='conversations'
    members = models.ManyToManyField(User, related_name='conversations')
    # datas registradas das conversações
    created_at = models.DateTimeField(auto_now_add=True)
    # saber quando foi modificado, adaptadi
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)       


class ConversationMessage(models.Model):
    # char baseado nas infos do model anterior, que são as mensagens, que serão deletadas ao deletar a conversa
    conversation = models.ForeignKey(ConversationArea, related_name='messages', on_delete=models.CASCADE)
    # conteúdo das mensagens
    content = models.TextField()
    # quando a mensagem foi criada
    created_at = models.DateTimeField()
    # quem criou a mensagem - deletada se deletar o usuário
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

# registra no admin do app!!
