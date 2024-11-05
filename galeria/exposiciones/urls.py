

from django.urls import path
from . import views
urlpatterns = [
    path("", views.ver_exposiciones, name="ver_exposiciones" ),
    path("exposiciones-futuras/", views.ver_exposiciones_futuras, name="ver_exposiciones_futuras" ),
    path("exposiciones-futuras/eliminar-exposiciones/", views.eliminar_exposiciones, name="eliminar_exposiciones" ),

]
