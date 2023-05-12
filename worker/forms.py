from django import forms
from .models import Member

INPUT_CLASSES = 'form-control form-control-md'

# ModelForm pois vou criar um form baseado num model que já existe, o Member
class NewMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'phone', 'email', 'company', 'image', 'description','profession',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'company': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'profession': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }
# agora vai criar o view