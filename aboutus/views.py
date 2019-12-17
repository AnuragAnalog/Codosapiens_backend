from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def aboutus(request):
    return HttpResponse("<h2 style='color:blue;'>About Us is working</h2>")
