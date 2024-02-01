from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ClubHub/index.html')

def blog(request):
    return render(request, 'ClubHub/blog.html')


def about(request):
    return render(request, 'ClubHub/about.html')

def contact(request):
    return render(request, 'ClubHub/contact.html')

def project(request):
    return render(request, 'ClubHub/project.html')

def service(request):
    return render(request, 'ClubHub/service.html')

def team(request):
    return render(request, 'ClubHub/team.html')

def testimonial(request):
    return render(request, 'ClubHub/testimonial.html')
