from django.contrib import admin
from .models import ConversationArea, ConversationMessage

# Register your models here.

admin.site.register(ConversationArea)
admin.site.register(ConversationMessage)

# agora cria o "forms.py" deste app