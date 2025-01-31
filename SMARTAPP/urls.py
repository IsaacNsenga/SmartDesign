from . import views
from django.urls import path

urlpatterns = [
    path("",views.home, name="home"),
    path('service', views.service, name='service'),
    path('realisation', views.realisation, name='realisation'),
    path('blog', views.blog, name='blog'),
    path('propos', views.propos, name='propos'),
    path('contact', views.contact, name='contact'),
    path('offre', views.offre, name='offre'),
    path('silver', views.silver, name='silver'),
    path('gold', views.gold, name='gold'),
    path('diamond', views.diamond, name='diamond'),
]