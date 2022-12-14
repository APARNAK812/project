from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'superadmin/home.html')
def login(request):
    return render(request,'superadmin/login.html')
def index1(request):
    return render(request,'superadmin/index1.html')    