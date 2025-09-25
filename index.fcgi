#!/home2/juli6984/juliootto.dev.br/.venv/bin/python

import os, sys 
from flup.server.fcgi import WSGIServer 
from django.core.wsgi import get_wsgi_application 

# The rest of your code remains the same
sys.path.insert(0, "/home2/juli6984/juliootto.dev.br")
os.environ['DJANGO_SETTINGS_MODULE'] = "setup.settings" 

WSGIServer(get_wsgi_application()).run()
