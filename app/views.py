from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

#home com modo de pesquisa (busca)
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

#função de formulário
def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

#função de cadastro dos carros dentro do formulário, CREATE do CRUD
def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

#Função que pega os dados do BD pela Primary Key e exibe essas informações em tela
def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

#UPDATE do CRUD, utilizando o mesmo form do cadastro, para não criar um novo form e gerar redundancia
def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

#Função UPDATE em si
def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

#Função DELETE do CRUD
def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')

#Função de paginação para a home
# def home(request):
#     data = {}
#     all = Carros.objects.all()
#     paginator = Paginator(all, 2)
#     pages = request.GET.get('page')
#     data['db'] = paginator.get_page(pages)
#     return render(request, 'index.html', data)
