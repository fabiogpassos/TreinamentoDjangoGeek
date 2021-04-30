from django.contrib import admin
from .models import Cargo, Servico, Colaborador

# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'modificado', 'ativo')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
	list_display = ('servico', 'icone', 'modificado', 'ativo')


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cargo', 'modificado', 'ativo')
