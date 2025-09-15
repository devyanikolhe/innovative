from django.shortcuts import render, redirect
from .models import Customer,Service, Testimonial
from .models import Customer,Service,Appointment
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")   

def services(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "services.html", {
        "services": services,
        "testimonials": testimonials
    })
         

def contact(request):
    return render(request,"contact.html")  

def appointment(request):
    if not request.session.get("customer_id"):
        messages.error(request, "Please log in to book an appointment.")
        return redirect(f"/login/?next={request.path}")
    customer = Customer.objects.get(id=request.session["customer_id"])

    if request.method == "POST":
        service_id = request.POST.get("service")
        vehicle_type = request.POST.get("vehicle_type")
        vehicle_brand = request.POST.get("vehicle_brand")
        vehicle_model = request.POST.get("vehicle_model")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")

        try:
            service = Service.objects.get(id=service_id)

            Appointment.objects.create(
                customer=customer,
                service=service,
                vehicle_type=vehicle_type,
                vehicle_brand=vehicle_brand,
                vehicle_model=vehicle_model,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            )

            messages.success(request, "✅ Appointment booked successfully!")
            return redirect("appointment")  # reload page or redirect somewhere else

        except Service.DoesNotExist:
            messages.error(request, "Invalid service selected.")

    # ✅ For GET request, show appointment form
    services = Service.objects.all()
    return render(request, "appointment.html", {"services": services})

def login_view(request):
    next_url = request.GET.get("next", "/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            customer = Customer.objects.get(username=username)
            print(password,customer.password)
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id
                request.session["customer_name"] = customer.name
                return redirect(next_url)
            else:
                messages.error(request, "Invalid password.")
        except Customer.DoesNotExist:
            messages.error(request, "User does not exist.")

        return redirect(f"/login/?next={next_url}")

    return render(request, "login.html", {"next": next_url})

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