from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,'index.html')
def attributs(request):
    return render(request,'attributs.html')

