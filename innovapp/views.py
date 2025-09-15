from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Customer
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")   

def services(request):
    return render(request,"services.html")      

def contact(request):
    return render(request,"contact.html")  

def appointment(request):
    return render(request,"appointment.html") 

from django.shortcuts import render, redirect
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            customer = Customer.objects.get(username=username)
            print(password,customer.password)
            if check_password(password, customer.password):
                # ✅ Save session manually
                request.session["customer_id"] = customer.id
                request.session["customer_name"] = customer.name
                # messages.success(request, "Login successful!")
                return redirect("/")
            else:
                messages.error(request, "Invalid password.")
        except Customer.DoesNotExist:
            messages.error(request, "User does not exist.")

        return redirect("login")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        password = request.POST.get("passw")

        try:
            # Create a new customer
            customer = Customer.objects.create(
                name=name,
                username=username,
                phone_number=phone_number,
                address=address,
                password=make_password(password)
            )
            return render(request, "login.html", {"success": "Registration successful! You can now log in."})

        except IntegrityError:
            # Email must be unique, handle duplicate
            return render(request, "register.html", {"error": "Email already exists. Please use another one."})

    return render(request, "register.html")


def logout_view(request):
    request.session.flush()  # ✅ Clears all session data
    # messages.success(request, "You have been logged out successfully.")
    return redirect("/")