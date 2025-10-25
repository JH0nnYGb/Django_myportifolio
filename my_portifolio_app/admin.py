from django.contrib import admin
from .models import My_projects

# Register your models here.
@admin.register(My_projects)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'link_github')
    search_fields = ('title', 'year')