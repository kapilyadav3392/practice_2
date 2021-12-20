from django.shortcuts import render



def home(request):
    return render (request,'index.html')


def bg(request):
    return render (request, 'blog-grid.html')

# Create your views here.
