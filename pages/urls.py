from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('churches', views.church, name="churches"),
    path('ministries', views.ministry, name="ministries"),
    path('events', views.event, name="events"),
    path('leaders', views.leader, name="leaders"),
    path('contact', views.contact, name="contact"),
    path('leaders/staff', views.staff, name="staff"),
    path('leaders/doulos', views.doulos, name="doulos")
]
