from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appvendas.forms import *
from appvendas.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')

def contato(request):
    return render(request,'contato.html')

def exibirproduto(request,id_produto):
    produto=Produto.objects.get(id=id_produto)
    return render(request,'exibirproduto.html',{'produto':produto})

def produto_detail(request, pk):
    produto=Produto.objects.get(id=pk)
    return render(request, 'produto/produto_detail.html', {'produto':produto})

def produto_list(request):
    criterio=request.GET.get('criterio')
    if(criterio):
        produtos=Produto.objects.filter(descricao__contains=criterio)
    else:
        produtos = Produto.objects.all().order_by('descricao')
        criterio=""
    paginator = Paginator(produtos, 2)
    page = request.GET.get('page')
    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)
    dados={'produtos':produtos,'criterio':criterio, 'paginator':paginator,'page_obj':produtos}

    return render(request, 'produto/produto_list.html', dados)

def produto_new(request):
    if (request.method=="POST"):
        form=ProdutoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form=ProdutoForm()
        dados={'form':form}
        return render(request,'produto/produto_form.html',dados)

def produto_update(request,pk):
    produto=Produto.objects.get(id=pk)
    if (request.method=="POST"):
        form=ProdutoForm(request.POST,instance=produto)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form=ProdutoForm(instance=produto)
        dados={'form':form,'produto':produto}
        return render(request,'produto/produto_form.html',dados)

def produto_delete(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.delete()
    return redirect('produto_list')

def unidade_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        unidades=Unidade.objects.filter(descricao__contains=criterio).order_by('descricao')
    else:
        unidades=Unidade.objects.all().order_by('descricao')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(unidades,2)
    page=request.GET.get('page')
    try:
        unidades=paginator.page(page)
    except PageNotAnInteger:
        unidades=paginator.page(1)
    except EmptyPage:
        unidades=paginator.page(paginator.num_pages)

    dados={'unidades':unidades,'criterio':criterio,'paginator':paginator,'page_obj':unidades}
    return render(request, 'unidade/unidade_list.html', dados)
def unidade_detail(request, pk):
    unidade=Unidade.objects.get(id=pk)
    return render(request, 'unidade/unidade_detail.html', {'unidade':unidade})
def unidade_new(request):
    if (request.method=="POST"):
        form=UnidadeForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm()
        dados={'form':form}
        return render(request, 'unidade/unidade_form.html', dados)
def unidade_update(request,pk):
    unidade=Unidade.objects.get(id=pk)
    if (request.method=="POST"):
        form=UnidadeForm(request.POST,instance=unidade)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm(instance=unidade)
        dados={'form':form}
        return render(request, 'unidade/unidade_form.html', dados)
def unidade_delete(request,pk):
    unidade=Unidade.objects.get(id=pk)
    unidade.delete()
    return redirect('unidade_list')

def venda_list(request):
    vendas=Venda.objects.all()
    lista={'vendas':vendas}
    return render(request,'venda/venda_list.html',lista)

def venda_new(request):
    if(request.method=='POST'):
        form=VendaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('venda_list')
    else:
        form=VendaForm()
        dados={'form':form}
        return render(request,'venda/venda_form.html',dados)

def cliente_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        clientes=Cliente.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        clientes=Cliente.objects.all().order_by('nome')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(clientes,2)
    page=request.GET.get('page')
    try:
        clientes=paginator.page(page)
    except PageNotAnInteger:
        clientes=paginator.page(1)
    except EmptyPage:
        clientes=paginator.page(paginator.num_pages)

    dados={'clientes':clientes,'criterio':criterio,'paginator':paginator,'page_obj':clientes}
    return render(request, 'cliente/clientes.html', dados)

def cliente_detail(request, pk):
    cliente = Cliente.objects.get(id=pk)
    return render(request,'cliente/cliente_detail.html', {'cliente':cliente})

def unidade_detail(request, pk):
    unidade=Unidade.objects.get(id=pk)
    return render(request, 'unidade/unidade_detail.html', {'unidade':unidade})

def cliente_update(request,pk):
    cliente=Cliente.objects.get(id=pk)
    if(request.method=='POST'):
        form=ClienteForm(request.POST,instance=cliente)
        if(form.is_valid()):
            form.save()
            return redirect('cliente_list')
    else:
        form=ClienteForm(instance=cliente)
        dados={'form':form,'cliente':cliente}
        return render(request,'cliente/cliente_form.html',dados)

def cliente_delete(request,pk):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()
    return redirect('clientes')

def cliente_new(request):
    if(request.method=='POST'):
        form=ClienteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('cliente_list')
    else:
        form=ClienteForm()
        dados={'form':form}
        return render(request,'cliente/cliente_form.html',dados)

def cargo_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        cargos=Cargo.objects.filter(descricao__contains=criterio).order_by('descricao')
    else:
        cargos=Cargo.objects.all().order_by('descricao')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(cargos,2)
    page=request.GET.get('page')
    try:
        cargos=paginator.page(page)
    except PageNotAnInteger:
        cargos=paginator.page(1)
    except EmptyPage:
        cargos=paginator.page(paginator.num_pages)

    dados={'cargos':cargos,'criterio':criterio,'paginator':paginator,'page_obj':cargos}
    return render(request, 'cargo/cargo_list.html', dados)

def cargo_new(request):
    if (request.method=="POST"):
        form=CargoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form=CargoForm()
        dados={'form':form}
        return render(request,'cargo/cargo_form.html',dados)

def cargo_update(request,pk):
    cargo=Cargo.objects.get(id=pk)
    if (request.method=="POST"):
        form=CargoForm(request.POST,instance=cargo)
        if (form.is_valid()):
            form.save()
            return redirect('cargo_list')
    else:
        form=CargoForm(instance=cargo)
        dados={'form':form}
        return render(request, 'cargo/cargo_form.html', dados)

def cargo_delete(request,pk):
    cargo=Cargo.objects.get(id=pk)
    cargo.delete()
    return redirect('cargo_list')

def funcionario_list(request):
    criterio=request.GET.get('criterio')
    if(criterio):
        funcionarios=Funcionario.objects.filter(nome__contains=criterio)
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio=""
    paginator = Paginator(funcionarios, 2)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados={'funcionarios':funcionarios,'criterio':criterio, 'paginator':paginator, 'page_obj':funcionarios}

    return render(request, 'funcionario/funcionario_list.html', dados)

def funcionario_detail(request, pk):
    funcionario=Funcionario.objects.get(id=pk)
    return render(request, 'funcionario/funcionario_detail.html', {'funcionario':funcionario})

def funcionario_new(request):
    if (request.method=="POST"):
        form=FuncionarioForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
        dados={'form':form}
        return render(request, 'funcionario/funcionario_form.html', dados)

def funcionario_update(request,pk):
    funcionario=Funcionario.objects.get(id=pk)
    if (request.method=="POST"):
        form=FuncionarioForm(request.POST,instance=funcionario)
        if (form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm(instance=funcionario)
        dados={'form':form}
        return render(request, 'funcionario/funcionario_form.html', dados)

def funcionario_delete(request,pk):
    funcionario=Funcionario.objects.get(id=pk)
    funcionario.delete()
    return redirect('funcionario_list')