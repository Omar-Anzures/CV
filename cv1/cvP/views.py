from django.shortcuts import render
from django.views import View
#primero importamos las de x defecto yt luego las que creamos
from .models import WorkExperience,Education,Skills

#cremos metodo get porque vamos a leer
#metodo view clase basada en vista
class Index(View):
    def get(self,request):
        template_name='index.html'
        work=WorkExperience.objects.all()#trae todos los objetos
        education=Education.objects.all()
        skills=Skills.objects.all()
        #agrega un solo regsitrop get y mandar el parametro que queremos en especifico
        #work=WorkExperience.objects.get(id=1)
        #work=WorkExperience.objects.last() trae el primer objeto de la BD
        #work=WorkExperience.objects.firts() trae el ultimo objeto de la BD
        #work=WorkExperience.objects.filter(name='Nix') Django Queryset trae todos los objetos filtrados osea lo que le especifiquemos
        context=dict(work=work,education=education,skills=skills)#guarda todo lo que va a usar en el template y puedan ver los usurarios
        #otra forma seria context={'works'=works} llave-valor

        return render(request,template_name,context)


class WorkExperienceView(View):
    def get(self,request):
        template_name='works.html'
        work=WorkExperience.objects.all()
        context=dict(work=work)
        return render(request,template_name,context)

class EducationView(View):
    def get(self,request):
        template_name='education.html'
        education=Education.objects.all()
        context=dict(education=education)
        return render(request,template_name,context)

class SkillsView(View):
    def get(self,request):
        template_name='skills.html'
        skills=Skills.objects.all()
        context=dict(skills=skills)
        return render(request,template_name,context)




