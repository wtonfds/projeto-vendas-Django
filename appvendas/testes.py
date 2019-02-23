from appvendas.models import *

lista_produtos=Produto.objects.filter(valorUnitario__gt=5).order_by('descricao')
for produto in lista_produtos:
    print("{0:s}-{1:.2f}".format(produto.descricao,
                                 produto.valorUnitario))

