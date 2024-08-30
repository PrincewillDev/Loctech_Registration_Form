from django.db import models
import uuid
# Create your models here.

class StudentReg(models.Model):
    FULL_PAYMENT = 'full payment'
    PART_PAYMENT = 'part payment'
    
    STANDARD = 'standard'
    CORPORATE = 'corporate'
    EXECUTIVE = 'executive'

    PAYMENT_CHOICES = [
        (FULL_PAYMENT, 'Full Payment'),
        (PART_PAYMENT, 'Part Payment'),
    ]
    
    TRAINING_CHOICES = [
        (STANDARD, 'Standard'),
        (CORPORATE, 'Corporate'),
        (EXECUTIVE, 'Executive'),
    ]


    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False) 
    email = models.EmailField(null=False, blank=False, max_length=100)
    address = models.CharField(max_length=255, blank=False, null=False)
    Qualification = models.CharField(max_length=100, blank=False, null=False)
    next_of_kin = models.CharField(max_length=100, blank=False, null=False)
    course = models.CharField(max_length=100, blank=False, null=False)
    occupation = models.CharField(max_length=100, blank=False, null=False)
    hear_about_us = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    state_of_origin = models.CharField(max_length=50, blank=False, null=False)
    course_duration = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    instructor = models.CharField(max_length=100, blank=False, null=False)
    type_of_training = models.CharField(max_length=50, choices= TRAINING_CHOICES, default=STANDARD, blank=False, null=False)
    payment_plan = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default=FULL_PAYMENT, blank=False, null=False)
    registering_officer = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return self.name