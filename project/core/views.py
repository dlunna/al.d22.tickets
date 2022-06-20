from django.shortcuts import render, HttpResponse

# Create your views here.

def root(request):
    return render(request, "core/root.html")

def about(request):
    return render(request, "core/about.html")
