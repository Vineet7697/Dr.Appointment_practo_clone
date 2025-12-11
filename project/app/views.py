from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import UserRegistration
from django.contrib.auth.hashers import make_password

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')



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


from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import UserRegistration
from django.contrib.auth.hashers import make_password, check_password


def base(request):
    return render(request,'base.html')


def home(request):
    return render(request,'home.html')


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



def register(request):
    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        country_code = request.POST.get('country_code')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        receive_offers = bool(request.POST.get('receive_offers'))

        if UserRegistration.objects.filter(email=email).exists():
            return render(request, 'register.html', {'x': 'Email already exists'})

        UserRegistration.objects.create(
            full_name=full_name,
            email=email,
            country_code=country_code,
            mobile=mobile,
            password=make_password(password),   # Already hashed
            allow_promotional=receive_offers,
        )

        return redirect('login')

    return render(request, "register.html")



def login(req):
    if req.method == "POST":
        le = req.POST.get('email')
        lp = req.POST.get('password')

        user = UserRegistration.objects.filter(email=le)

        if user:
            userdata = UserRegistration.objects.get(email=le)

            # 🚀 CHANGE #1: Correct password checking
            if check_password(lp, userdata.password):

                # Original variables — untouched
                id = userdata.id
                name = userdata.full_name
                email = userdata.email
                mobile = userdata.mobile
                password = userdata.password

                data = {'id': id, 'name': name, 'email': email, 'mobile': mobile, 'password': password}

                # Original redirect — untouched
                base_url = reverse('dashboard')
                data = urlencode(data)
                url = f'{base_url}?{data}'
                return redirect(url)

            else:
                msg = "Email and password not matched"
                return render(req, 'login.html', {'msg': msg})
        else:
            msg = "Email id not register"
            return render(req, 'register.html', {'msg': msg, 'email': le})

    return render(req, "login.html")



def dashboard(req):
    e = req.GET.get('email')
    p = req.GET.get('password')
    
    if e and p:
        i = req.GET.get('id')
        n = req.GET.get('name')
        m = req.GET.get('mobile')

        data = {'name': n, 'mobile': m, 'id': i}
        return render(req, 'dashboard.html', {'data': data})

    else:
        return redirect('login')
