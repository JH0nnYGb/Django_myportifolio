from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MyProjects
from .models import MyActivities
# Create your views here.

def home(request):
    return render(request,'home.html')

def project(request):
    projects = MyProjects.objects.all().order_by('-year_project')
    pagination = Paginator(projects, 4)

    page_number = request.GET.get('page')#numeros de paginas no total
    page_obj = pagination.get_page(page_number)#numero da pagina de um certo objeto(ordenação)

    return render(request,'projects.html', {'page_obj': page_obj})

def activities(request):
    atividades = MyActivities.objects.all().order_by('-year_activ')
    paginator = Paginator(atividades, 4)  # 4 atividades por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'activities.html', {'page_obj': page_obj})