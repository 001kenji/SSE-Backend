from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.index,name='index file'),
    path("stream/",views.trial1, name="first test of sse")


]

