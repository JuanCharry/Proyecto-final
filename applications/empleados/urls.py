from django.urls import path , re_path , include
from rest_framework import routers
from . import views


app_name = 'empleado_app'

router = routers.DefaultRouter()
router.register(r'/empleados', views.AdminView)

urlpatterns = [
    path(
        'api/persona/list',
        views.EmpleadosApiView.as_view(),
    ),



    path(
        'api/persona/list/<pk>',
        views.UpdateEmpleadosApiView.as_view(),
    ),
    
    path(
        'gestion/humana', include(router.urls)
    )
] 