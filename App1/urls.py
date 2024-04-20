from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #HOME
    path("",views.inicio,name="inicio"),
    path("login", views.login_request , name="login"),
    path("register", views.register, name="Register"),
    path("logout",LogoutView.as_view (template_name="logout.html"),name="Logout"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),


    #CURSOS
    path("curso_alta", views.curso_formulario),
    path("cursos", views.cursos_ver,name="cursos"),
    path("curso_buscar",views.curso_buscar),
    path("curso_resultado",views.curso_resultado),
    path("curso_eliminar/<int:id>", views.curso_eliminar, name="curso_eliminar"),
    path("curso_editar/<int:id>", views.curso_editar,name="curso_editar"),
    
    #PROFESORES
    path("profesores",views.profesores_ver),
    path("profesor_alta",views.profesor_formulario),
    path("profesor_buscar",views.profesor_buscar),
    path("profesor_resultado",views.profesor_resultado),
    path("profesor_eliminar/<int:id>", views.profesor_eliminar, name="profesor_eliminar"),
    path("profesor_editar/<int:id>", views.profesor_editar,name="profesor_editar"),


    #ALUMNOS
    path("alumnos",views.alumnos_ver),
    path("alumno_alta",views.alumno_formulario),
    path("alumno_buscar",views.alumno_buscar),
    path("alumno_resultado", views.alumno_resultado),
    path("alumno_eliminar/<int:id>", views.alumno_eliminar, name="alumno_eliminar"),
    path("alumno_editar/<int:id>", views.alumno_editar,name="alumno_editar"),
]
