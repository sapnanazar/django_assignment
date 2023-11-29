from django.shortcuts import render


def home(request):

    return render(request, "home.html")

def index(request):

    value1 = request.GET['name']
    value2 = request.GET['reg']
    value3 = request.GET['dept']



    context = {'name': value1, 'reg': value2, 'dept': value3}

    
    return render(request, "index.html",context )