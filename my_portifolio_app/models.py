from django.db import models

# Create your models here.

class MyProjects(models.Model):
    title_project = models.CharField(max_length=100, verbose_name= "Título do Projeto")
    image_porject = models.ImageField(upload_to='projetos/', blank=True, null=True)
    summary = models.CharField(verbose_name= "Resumo Projeto")
    year_project = models.PositiveBigIntegerField(verbose_name="Ano do Projeto")
    link_github = models.URLField(verbose_name="Link do Reposistório no GitHub")
    
    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
        ordering = ['-year_project'] # exibe os mais recentes primeiro

    def  __str__(self):
        return f"{self.title_project} ({self.year_project})"
    
class MyActivities(models.Model):
    title_activ = models.CharField(max_length=100, verbose_name= "Título da atividade")
    summary_activ = models.CharField(max_length=250, verbose_name="Resumo sobre atividade")
    year_activ =  models.PositiveBigIntegerField(verbose_name="Ano da atividade")
    image_activ = models.ImageField(upload_to='projetos/', blank=True, null=True)

    class Meta:
        verbose_name = "Activitie"
        verbose_name_plural = "My Activities"
        ordering = ['-year_activ'] # exibe os mais recentes primeiro

    def __str__(self):
        return f"{self.title_activ} ({self.year_project})"