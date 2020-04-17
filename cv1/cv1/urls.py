from django.contrib import admin
from django.urls import path
from django.conf import settings#importamos nuestra configuracion
from django.conf.urls.static import static


from cvP.views import Index,WorkExperienceView,EducationView,SkillsView

urlpatterns = [
    path('admin/', admin.site.urls),
    #siempre que queremos usar clases basadas en vistas
    #tenemos que usar as_view() de la clase
    path('',Index.as_view()),
    path('skills',SkillsView.as_view(),name='skills'),
    path('education',EducationView.as_view(),name='education'),
    path('works',WorkExperienceView.as_view(),name='works'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#concatenamos las url para poder utilizar media y poder acceder a ella y que django púeda acceder a ella 
