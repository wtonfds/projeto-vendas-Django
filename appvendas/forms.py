from django.forms import ModelForm
from .models import * 

class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')

class ProdutoForm(ModelForm):
    class Meta:
        model=Produto
        fields=('descricao','unidade','valorUnitario')

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=('nome','email','telefone','endereco')

class FuncionarioForm(ModelForm):
	class Meta:
		model = Funcionario
		fields=('nome', 'matricula', 'cargo', 'telefone', 'email')

class CargoForm(ModelForm):
  class Meta:
    model = Cargo
    fields=('descricao',)
