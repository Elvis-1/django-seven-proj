from django.urls import path
from . import views

urlpatterns = [
    # path('',views.test, name='test'),
    path('',views.signup, name='signup'),
    path('loginn/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('mypost/',views.myPost, name='mypost'),
    path('newpost/',views.newPost, name='newpost'),
    path('signout/',views.signout,name='signout'),
]