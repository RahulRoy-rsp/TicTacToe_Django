from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def vsComp(request):
    return render(request, 'vsComp.html')

def oneVsone(request):
    return render(request, 'oneVsone.html')