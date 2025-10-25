from django.shortcuts import render
from django.core.paginator import Paginator
from .models import My_projects
# Create your views here.

def home(request):
    return render(request,'home.html')

def project(request):
    projects = My_projects.objects.all().order_by('-year')
    pagination = Paginator(projects, 4)

    page_number = request.GET.get('page')#numeros de paginas no total
    page_obj = pagination.get_page(page_number)#numero da pagina de um certo objeto(ordenação)

    return render(request,'projects.html', {'page_obj': page_obj})