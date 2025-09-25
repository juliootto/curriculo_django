from django import forms   
from curriculo.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = []
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'telefone': 'Telefone',
            'mensagem': 'Mensagem',
        }
        help_texts = {
            'nome': 'Nome Completo',
            'email': 'seunome@dominio.com',
            'telefone': '(XX) XXXXX-XXXX)',
            'mensagem': 'Sua mensagem aqui',
        }

        widgets = { 
                    'nome': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'telefone': forms.TextInput(attrs={'class': 'form-control'}),
                    'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
                    }


