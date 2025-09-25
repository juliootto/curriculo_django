# Deploy de um Projeto Django no HostGator com FCGI

Este guia fornece instruções passo a passo para implantar um projeto Django em um ambiente de hospedagem compartilhada do HostGator usando FCGI.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte:

- Acesso SSH à sua conta HostGator.
- Os arquivos do seu projeto Django prontos para upload.
- Um arquivo `requirements.txt` listando as dependências do seu projeto.

Primeiro, verifique a versão do Python em execução no seu servidor e garanta que seu projeto e suas bibliotecas sejam compatíveis.

## Guia Passo a Passo

### 1. Configurar o Ambiente Virtual

1.  **Baixar o `virtualenv`**

    Navegue até o diretório raiz do seu domínio (ex: `seudominio.com.br`) via SSH e baixe uma versão específica do `virtualenv`.

    ```bash
    curl --location --output virtualenv.tar.gz https://github.com/pypa/virtualenv/tarball/16.7.9
    ```

2.  **Extrair o pacote**

    ```bash
    tar -xvzf virtualenv.tar.gz
    ```

3.  **Criar o ambiente**

    Isso criará um diretório `.venv` contendo o interpretador Python e as bibliotecas. O nome da pasta extraída (ex: `pypa-virtualenv-34c62ba`) pode variar.

    ```bash
    python pypa-virtualenv-34c62ba/virtualenv.py .venv
    ```

4.  **Limpeza**

    Agora você pode remover o arquivo compactado baixado e a pasta extraída.

    ```bash
    rm virtualenv.tar.gz
    rm -rf pypa-virtualenv-34c62ba
    ```

### 2. Ativar o Ambiente e Instalar Dependências

1.  **Ativar o ambiente**

    ```bash
    source .venv/bin/activate
    ```

2.  **Instalar as dependências do projeto**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Instalar bibliotecas FCGI**

    ```bash
    pip install flup
    pip install django-wsgi
    ```

### 3. Configurar o Servidor

1.  **Fazer upload do seu projeto**

    Certifique-se de que todos os arquivos do seu projeto Django foram enviados para o servidor, dentro do diretório onde você criou o `.venv`.

2.  **Criar arquivo `.htaccess`**

    Crie um arquivo chamado `.htaccess` no diretório raiz do seu projeto com o seguinte conteúdo. Isso redirecionará as requisições para o seu arquivo `index.fcgi`.

    ```apache
    Options +ExecCGI
    AddHandler fcgid-script .fcgi
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ index.fcgi/$1 [QSA,L]
    ```

3.  **Criar arquivo `index.fcgi`**

    Crie um arquivo chamado `index.fcgi`. Este script é o ponto de entrada para sua aplicação.

    **Importante:** Substitua `/homeX/CONTA/PASTA_DO_SITE` pelo caminho absoluto para o diretório do seu projeto e `setup.settings` pelo módulo de configurações do seu projeto.

    ```python
    #!/homeX/CONTA/PASTA_DO_SITE/.venv/bin/python

    import os, sys
    from flup.server.fcgi import WSGIServer
    from django.core.wsgi import get_wsgi_application

    # Adicione seu projeto ao Python path
    sys.path.insert(0, "/homeX/CONTA/PASTA_DO_SITE")
    os.environ['DJANGO_SETTINGS_MODULE'] = "setup.settings"

    WSGIServer(get_wsgi_application()).run()
    ```

4.  **Definir permissões**

    Torne o arquivo `index.fcgi` executável.

    ```bash
    chmod 0755 index.fcgi
    ```

### 4. Configurar o Django

1.  **Modificar o `settings.py`**

    Adicione seu domínio à lista `ALLOWED_HOSTS` no arquivo `settings.py` do seu projeto.

    ```python
    ALLOWED_HOSTS = ['seudominio.com.br', 'www.seudominio.com.br']
    ```

### Verificação Final

Seu site já deve estar no ar! Se encontrar algum problema, verifique os logs de erro do servidor para mais detalhes.

