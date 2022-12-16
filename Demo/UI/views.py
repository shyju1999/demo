from django.shortcuts import render

# Create your views here.
def homepage (request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def change_dp(request):
    return render(request,"change_dp.html")

def upload_resume(request):
    return render(request,"upload_resume.html") 