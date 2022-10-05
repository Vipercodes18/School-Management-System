from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"Yeh send Ho gaya hai"
    }
    return render(request, 'index.html', context )
    #return HttpResponse("Welcome to Future")

def Services(request):
    return render(request, 'Services.html')
    #return HttpResponse("Enter the Name of Student")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("Enter the Class and Section")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("Welcome to Our Online School Management System")
