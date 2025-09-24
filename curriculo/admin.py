from django.contrib import admin
from curriculo.models import Escolaridade, ExperienciaProficional, Cursos, Contato, Interesses

# Register your models here.

class EscolaridadeAdmin(admin.ModelAdmin):
    list_display = ('id','instituicao_ensino', 'curso', 'inicio', 'fim')
    search_fields = ('instituicao_ensino', 'curso')

class ExperienciaProficionalAdmin(admin.ModelAdmin):
    list_display = ('id','empresa', 'cargo', 'inicio', 'fim')
    search_fields = ('empresa', 'cargo')

class CursosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'empresa', 'inicio', 'fim')
    search_fields = ('nome', 'empresa')

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'telefone')
    search_fields = ('nome', 'email', 'telefone')

class InteressesAdmin(admin.ModelAdmin):
    list_display = ('id','interesse',)
    search_fields = ('interesse',)

admin.site.register(Escolaridade, EscolaridadeAdmin)
admin.site.register(ExperienciaProficional, ExperienciaProficionalAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Interesses, InteressesAdmin)