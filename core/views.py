from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def root_view(request):
    return HttpResponse("Welcome to SmartMCP - Model Context Protocol API System")