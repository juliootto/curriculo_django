from django.urls import path
from curriculo.views import index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',index,name='index'),

]

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.CERTIFICADO_URL, document_root=settings.CERTIFICADO_ROOT)