from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('team/',views.team),
    path('contact/',views.contact),
    path('service/',views.service),
    path('testimonial/',views.testimonial),
    path('project/',views.project)
]
