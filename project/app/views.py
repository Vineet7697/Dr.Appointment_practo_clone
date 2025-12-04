from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def find_doctor(request):
    services = [
        {"icon": "fas fa-user-md", "text": "Consult with a doctor"},
        {"icon": "fas fa-shopping-cart", "text": "Order Medicines"},
        {"icon": "fas fa-file-medical", "text": "View medical records"},
        {"icon": "fas fa-flask", "text": "Book test"},
        {"icon": "fas fa-book", "text": "Read articles"},
        {"icon": "fas fa-briefcase", "text": "For healthcare providers"},
    ]
    return render(request,'find_doctor.html',{"service":services})

def video_consult(request):
    return render(request,'video_consult.html')

def surgeries(request):
    return render(request,'surgeries.html')

def footer(request):
    return render(request,'footer.html')

def register(req):
    return render(req,'register.html')