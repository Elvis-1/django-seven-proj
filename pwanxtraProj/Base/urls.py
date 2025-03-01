from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/',views.about_us,name='about'),

    # estates

    path('AkaEzePhase2/',views.akaEzePhase2, name='AkaEzePhase2'),
    path('isura/',views.isuraPhase2, name='isura'),
    path('ngozi/',views.ngozi, name='ngozi'),
    path('ikenga/',views.ikenga,name='ikenga'),
    path('nkem/',views.nkem, name='nkem'),
    path('Aku/',views.Aku, name='Aku'),
    path('ileri/',views.ileri, name='ileri'),
    path('ileAyo3/',views.IleAyo3, name='IleAyo3'),
    path('Enyiaba2/',views.Enyiaba2, name='Enyiaba2'),


    path('soldout/',views.soldout, name='soldout'),
    path('contact/',views.contact, name='contact'),


    path('services/',views.services, name='services'),
]