from django.db import models

# Create your models here.

class My_projects(models.Model):
    title = models.CharField(max_length=100, verbose_name= "Título do Projeto")
    image_porject = models.ImageField(upload_to='projetos/', blank=True, null=True)
    summary = models.CharField(verbose_name= "Resumo Projeto")
    year = models.PositiveBigIntegerField(verbose_name="Ano do Projeto")
    link_github = models.URLField(verbose_name="Link do Reposistório no GitHub")
    
    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
        ordering = ['-year'] # exibe os mais recentes primeiro

    def  __str__(self):
        return f"{self.title} ({self.year})"