from django.shortcuts import render
from .models import male_clothes
from .models import female_clothes
from django.views.generic import DetailView

def index(request):
    return render(request, 'main/index.html')

def male(request):
    male = male_clothes.objects.all()
    return render(request, 'main/male.html', {'male': male})

def female(request):
    female = female_clothes.objects.all()
    return render(request, 'main/female.html', {'female': female})


class MainDetailModelMale(DetailView):
    model = male_clothes
    template_name = 'main/new_page.html'
    context_object_name = 'newPage'

class MainDetailModelFemale(DetailView):
    model = female_clothes
    template_name = 'main/new_page.html'
    context_object_name = 'newPage'