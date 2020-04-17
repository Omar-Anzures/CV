from django.contrib import admin
from .models import WorkExperience,Education,Skills

#decorador que va ligado al modelo
@admin.register(WorkExperience)
#paso por medio del decorador la clase y como quiere que se vea en el admmon
class workExperencieAdmin(admin.ModelAdmin):
    list_display = ['name','start_year','end_year','actual_job']
#OTRA FORMA DE HACER LO DE ARRIBA ES: pero hay diferencfia
#en el admin
#admin.site.register(Education)
#para sobre escribir el metodo tenemos que hacerlo desde models
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name','school_name','start_year','end_year']


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','level']



