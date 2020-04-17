from django.db import models
#MODELOS BASADOS EN VISTA
#siempre vamos a poner el metodo str
class WorkExperience(models.Model):
    name=models.CharField(max_length=250)
    start_year = models.DateField()
    #atributo blank,campo en blanco true y false viseversa
    #null =false o true ´para indicar a BD automaticamente si es false te agrega un string vacio
    end_year = models.DateField(blank=True,null=True)
    job_title =models.CharField(max_length=250)
    actual_job = models.BooleanField(default=False)
    description = models.TextField() 
    def __str__(self):
        return 'Trabaje en {}'.format(self.name)

class Education(models.Model):
    name=models.CharField(max_length=250)
    school_name = models.CharField(max_length=250)
    start_year = models.DateField()
    end_year = models.DateField(blank=True,null=True)
    #para mostrar el nombre del registro que agregamos en el admin
    #xq x defento tiene Education.object1
    def __str__(self):
        return self.name

class Skills(models.Model):
    LEVEL_CHOICES=(
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced')
    )
    name=models.CharField(max_length=255)
    level=models.CharField(choices=LEVEL_CHOICES,max_length=15,blank=True,null=True)
    icon=models.ImageField(upload_to='icons/',max_length=350)
    porcentage=models.PositiveSmallIntegerField(default=60,null=False,blank=False)
    def __str__(self):
        #segun el nombre del atributo get level y solo es valido con choice
        return '{} - Level: {}'.format(self.name,self.get_level_display())

