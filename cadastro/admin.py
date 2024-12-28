from django.contrib import admin
from .models import Produto, Fornecedor, LocalArmazenamento, CentroDistribuicao, Profissional


class BaseModelAdmin(admin.ModelAdmin):
    """
    Configuração base para exibição e gerenciamento de models com campos comuns.
    """
    readonly_fields = ('data_adicionado', 'data_alterado')
    list_display = ('id', 'data_adicionado', 'ativo')
    list_display_links = ('id',)
    list_filter = ('ativo',)
    search_fields = ('id',)
    ordering = ('id',)
    fieldsets = (
        ("Informações Gerais", {
            'fields': ('id', 'ativo')
        }),
    )


@admin.register(Produto)
class ProdutoAdmin(BaseModelAdmin):
    list_display = ('codigo', 'nome', 'estoque_minimo', 'ativo')
    list_display_links = ('codigo',)
    search_fields = ('codigo',)
    list_filter = ('ativo',)
    fieldsets = (
        ("Informações do Produto", {
            'fields': ('codigo', 'nome', 'estoque_minimo', 'custo_unitario', 'unidade_medida', 'ativo')
        }),
    )


@admin.register(Fornecedor)
class FornecedorAdmin(BaseModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'ativo')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('ativo',)
    fieldsets = (
        ("Informações do Fornecedor", {
            'fields': ('nome', 'email', 'telefone', 'observacoes', 'ativo')
        }),
    )


@admin.register(LocalArmazenamento)
class LocalArmazenamentoAdmin(BaseModelAdmin):
    list_display = ('nome', 'ativo', 'data_adicionado')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('ativo',)
    fieldsets = (
        ("Informações do Local", {
            'fields': ('nome', 'observacoes', 'ativo')
        }),
    )


@admin.register(CentroDistribuicao)
class CentroDistribuicaoAdmin(BaseModelAdmin):
    list_display = ('nome', 'responsavel', 'telefone', 'ativo')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('ativo',)
    fieldsets = (
        ("Informações do Centro", {
            'fields': ('nome', 'endereco', 'responsavel', 'telefone', 'ativo')
        }),
    )


@admin.register(Profissional)
class ProfissionalAdmin(BaseModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'ativo')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('ativo',)
    fieldsets = (
        ("Informações do Profissional", {
            'fields': ('nome', 'email', 'telefone', 'ativo')
        }),
    )
