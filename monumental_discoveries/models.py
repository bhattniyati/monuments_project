from django.db import models
from datetime import datetime


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

LANGUAGE_CHOICES = (
        ('hindi', 'Hindi'),
        ('english', 'English'),
        ('gujarati', 'Gujarati')
    )

STATUS = (
        ('success', 'Success'),
        ('pending', 'Pending'),
        ('failed', 'Failed')
    )

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.BigIntegerField(blank=True, null=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    address=models.TextField()
    password=models.CharField(max_length=20)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.email

class State(models.Model):
    state_name=models.CharField(max_length=30)

class City(models.Model):
    state_id=models.ForeignKey(State, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=20)

class Guide(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20, blank=True, null=True)
    email=models.EmailField()
    phone_no=models.BigIntegerField(blank=True, null=True)
    password=models.CharField(max_length=20)
    status=models.BooleanField(default=True)

class Monuments(models.Model):
    state_id=models.ForeignKey(State, on_delete=models.CASCADE)
    city_id=models.ForeignKey(City, on_delete=models.CASCADE)
    monuments_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to ='monuments_images')
    monument_location=models.CharField(max_length=256)
    ticket_price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField()

class Audio(models.Model):
    monuments_id=models.ForeignKey(Monuments, on_delete=models.CASCADE)
    audio_file=models.FileField(upload_to='monuments_audio')
    audio_language=models.CharField(max_length=30,choices=LANGUAGE_CHOICES)

class GuideBooking(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    guide_id=models.ForeignKey(Guide, on_delete=models.CASCADE)
    monuments_id=models.ForeignKey(Monuments, on_delete=models.CASCADE)
    booking_datetime=models.DateTimeField(default=datetime.now, blank=True)
    rate=models.DecimalField(max_digits=6, decimal_places=2)
    status=models.CharField(max_length=30,choices=STATUS)

class TicketBooking(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    booking_datetime=models.DateTimeField(default=datetime.now, blank=True)
    monuments_id=models.ForeignKey(Monuments, on_delete=models.CASCADE)
    number_of_person=models.IntegerField()
    status=models.CharField(max_length=30,choices=STATUS)

class Payment(models.Model): 
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    guide_booking_id=models.ForeignKey(GuideBooking, on_delete=models.CASCADE)
    ticket_booking_id=models.ForeignKey(TicketBooking, on_delete=models.CASCADE)
    payment_amount=models.DecimalField(max_digits=6, decimal_places=2)
    payment_receipt=models.CharField(max_length=256)
    payment_status=models.CharField(max_length=30,choices=STATUS)

class Feedback(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.CharField(max_length=20)

class Complain(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    guide_id=models.ForeignKey(Guide, on_delete=models.CASCADE)
    comment=models.TextField()






