from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models.Tutor import Tutor
from .models.Assessment import Assessment
from .models.Institution import Institution


def index(request):
    if request.method == 'GET':
        return HttpResponse('get view')
    
    if request.method == 'POST':
        return HttpResponse('post view')


class TutorListView(ListView):
    model = Tutor
    context_object_name = 'tutor'
