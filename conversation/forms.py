from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        # para deixar estilizado:
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

# agora cria a view