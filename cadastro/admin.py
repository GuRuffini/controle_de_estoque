from django.contrib import admin
from .models import Produto, Fornecedor, LocalArmazenamento, CentroDistribuicao, Profissional


class BaseModelAdmin(admin.ModelAdmin):
    """
    Configuração base para exibição e gerenciamento de models com campos comuns.
    """
    readonly_fields = ('data_adicionado', 'data_alterado')
    list_display = ('id', 'data_adicionado')
    list_filter = ('ativo',)
    search_fields = ('id',)
    ordering = ('id',)
    

@admin.register(Produto)
class ProdutoAdmin(BaseModelAdmin):
    list_display = ('codigo', 'nome', 'estoque_minimo')
    search_fields = ('codigo', 'nome')
    list_filter = ('ativo',)


@admin.register(Fornecedor)
class FornecedorAdmin(BaseModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)


@admin.register(LocalArmazenamento)
class LocalArmazenamentoAdmin(BaseModelAdmin):
    list_display = ('nome', 'ativo', 'data_adicionado')
    search_fields = ('nome',)
    list_filter = ('ativo',)


@admin.register(CentroDistribuicao)
class CentroDistribuicaoAdmin(BaseModelAdmin):
    list_display = ('nome', 'responsavel', 'telefone')
    search_fields = ('nome', 'responsavel')
    list_filter = ('ativo',)


@admin.register(Profissional)
class ProfissionalAdmin(BaseModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)
