
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='my_index'),
    path('aboutus/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contact'),
    path('service/',views.service,name='my_service'),
    path('guard/',views.guard,name='my_guard'),

]