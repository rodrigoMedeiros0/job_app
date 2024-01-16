from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!!")

def job_detail(request, id):
    return HttpResponse(f"Job Detail Page: {id}")