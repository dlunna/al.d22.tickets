from django.urls import path
from . import views as binnacle_views

urlpatterns = [
    path('', binnacle_views.reporte, name="demo"),
]