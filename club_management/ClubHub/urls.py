from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.index, name = 'index'),
    path('About', views.about, name = 'about'),
    path('Our Blog Our Team Testimonial 404 Page', views.blog, name = 'blog'),
    path('Contact', views.contact, name = 'contact'),
    path('Project', views.project, name = 'project'),
    path('Services', views.service, name = 'service'),
    path('', views.team, name = 'team'),
    path('', views.testimonial, name = 'testimonial'),

]