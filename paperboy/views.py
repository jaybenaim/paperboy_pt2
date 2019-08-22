from django.http import HttpResponse
from django.shortcuts import render, redirect
from paperboy.models import * 
from django import forms 

def root(request): 
    return redirect('') 

def home(request): 
    paperboy = Paperboy.objects.all() 
    context = { 
        'paperboy': paperboy 
    }
    return render (request, 'index.html', context)