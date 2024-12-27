from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Classe base para fornecer campos comuns de controle de log para outras models.
    """
    data_adicionado = models.DateTimeField(auto_now_add=True, verbose_name="Data de Adição")
    data_alterado = models.DateTimeField(auto_now=True, verbose_name="Última Alteração")
    usuario_adiciona = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_criado_por", verbose_name="Usuário que Adicionou")
    usuario_alteracao = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_alterado_por", verbose_name="Usuário que Alterou")
    ativo = models.BooleanField(default=True, verbose_name="Ativo", help_text="Indica se o registro está ativo no sistema.")

    class Meta:
        abstract = True
        ordering = ["id"]


class Produto(BaseModel):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    estoque_minimo = models.PositiveIntegerField(verbose_name="Estoque Mínimo")
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo Unitário")
    unidade_medida = models.CharField(max_length=10, verbose_name="Unidade de Medida")

    class Meta(BaseModel.Meta):
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Fornecedor(BaseModel):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta(BaseModel.Meta):
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome


class LocalArmazenamento(BaseModel):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta(BaseModel.Meta):
        verbose_name = "Local de Armazenamento"
        verbose_name_plural = "Locais de Armazenamento"

    def __str__(self):
        return self.nome


class CentroDistribuicao(BaseModel):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.TextField(verbose_name="Endereço")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    class Meta(BaseModel.Meta):
        verbose_name = "Centro de Distribuição"
        verbose_name_plural = "Centros de Distribuição"

    def __str__(self):
        return self.nome


class Profissional(BaseModel):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    class Meta(BaseModel.Meta):
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"

    def __str__(self):
        return self.nome
