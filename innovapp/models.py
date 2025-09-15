from django.db import models

# Customer
class Customer(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=20)
    username = models.CharField(unique=True,max_length=20)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# Service Provider / Mechanic

class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100, blank=True)
    availability_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Service
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=100)
    duration = models.CharField(max_length=100,help_text="Duration in minutes")
    icon = models.CharField(max_length=100, default="fas fa-cogs", help_text="Font Awesome class e.g. fas fa-tools")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# Appointment / Booking
class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    vehicle_type = models.CharField(max_length=50)
    vehicle_brand = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.customer.name} - {self.service.name} on {self.appointment_date}"

# Payment
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    )

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Payment for {self.appointment}"

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, help_text="e.g. Regular Customer, First-time Customer")
    feedback = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role if self.role else 'Customer'}"