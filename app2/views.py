from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app2(request):
    return HttpResponse('<h1>I WILL GET JOB</h1>')