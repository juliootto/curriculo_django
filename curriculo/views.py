from django.shortcuts import render, redirect
from curriculo.models import Cursos, ExperienciaProficional, Escolaridade, Interesses
from curriculo.forms import ContatoForm
from django.contrib import messages
from django.urls.base import reverse
from django.core.mail import send_mail 
from django.conf import settings 


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            # --- LÓGICA DE ENVIO DE E-MAIL ---
            try:
                # 2. Obtenha os dados limpos do formulário
                nome = form.cleaned_data['nome']
                email_remetente = form.cleaned_data['email']
                telefone = form.cleaned_data['telefone']
                mensagem = form.cleaned_data['mensagem']

                # 3. Construa a mensagem do e-mail
                subject = f'Nova mensagem de {nome}'
                message_body = f"""
                Você recebeu uma nova mensagem de contato através do seu site.

                Nome: {nome}
                Email: {email_remetente}
                Telefone: {telefone}

                Mensagem:
                {mensagem}
                """
                from_email = settings.EMAIL_HOST_USER
                # Coloque aqui o seu e-mail para onde você quer receber a notificação
                recipient_list = [settings.EMAIL_DESTINATION,] 
                print("--- TENTANDO ENVIAR E-MAIL ---")
                print(f"Assunto: {subject}")
                print(f"De: {from_email}")
                print(f"Para: {recipient_list}")

                # 4. Envie o e-mail
                send_mail(subject, message_body, from_email, recipient_list)
                print("--- FUNÇÃO SEND_MAIL EXECUTADA SEM ERRO ---")
                
                messages.success(request, 'Mensagem enviada com sucesso!')

            except Exception as e:
                # Se algo der errado no envio, mostre uma mensagem de erro
                messages.error(request, 'Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.')
                print(e) # Para depuração no console
            
            return redirect(reverse('index') + '#contato')
    else:
        form = ContatoForm()
        
        
    # Contexto com todos os dados para exibir na página
    context = {
        'cursos': Cursos.objects.all().order_by('-fim'),
        'experiencia': ExperienciaProficional.objects.all().order_by('-inicio'),
        'escolaridade': Escolaridade.objects.all().order_by('-inicio'),
        'interesses': Interesses.objects.all().order_by('-id'),
        'form': form, # Passa o form vazio (no GET) ou o form com erros (no POST inválido)
    }

    return render(request, 'index.html', context)

