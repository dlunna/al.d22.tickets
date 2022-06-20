from django.urls import path
from . import views as core_views

urlpatterns = [
    path('acercade/', core_views.about, name="about"),
]
