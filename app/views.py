from django.shortcuts import render

# Create your views here.

def movies(request):
    return render(request,'movies.html')


def holly(request):
    return render(request,'holly.html')


def bolly(request):
    return render(request,'bolly.html')
