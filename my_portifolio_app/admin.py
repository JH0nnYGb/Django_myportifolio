from django.contrib import admin
from .models import MyProjects
from .models import MyActivities


# Register your models here.
@admin.register(MyProjects)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('title_project', 'year_project', 'link_github')
    search_fields = ('title_project', 'year_project')

@admin.register(MyActivities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title_activ', 'year_activ')
    search_fields = ('title_activ', 'year_activ')
