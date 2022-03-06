from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image



crop_CHOICES = [
    ("Rabi", "Rabi"),
    ("Wheat", "Wheat"),
    ("Barley", "Barley"),
    ("Mustard", "Mustard"),
    ("Sesame", "Sesame"),
    ("Peas", "Peas"),
    ("Kharif", "Kharif"),
    ("Bajra & Jowar", "Bajra & Jowar"),
    ("Cotton", "Cotton"),
    ("Soyabean", "Soyabean"),
    ("Sugarcane", "Sugarcane"),
    ("Turmeric", "Turmeric"),
    ("Paddy (Rice)", "Paddy (Rice)"),
    ("Maize", "	 Maize"),
    ("Moong (Pulses)", "Moong (Pulses)"),
    ("Groundnut", "Groundnut"),
    ("Red Chillies", "Red Chillies"),
    ("Zaid", "Zaid"),
    (" Prominent", " Prominent"),
    ("Muskmelon", "Muskmelon"),
    ("Watermelon", "Watermelon"),
    (" bitter gourd", " bitter gourd"),
    ("pumpkin", "pumpkin"),
    ("ridged gourd", "ridged gourd"),
]
state_choices = [
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"),
    ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"),
]
gender_CHOICES = [("MALE", "MALE"), ("FEMALE", "FEMALE")]


class Shareinformation(models.Model):
    sharee = models.TextField(null=False)
    email = models.EmailField()
    
    def __str__(self):

        return self.email
    

class Personhomepage(models.Model):
     user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        
        on_delete=models.CASCADE,
       
       
     )
     personimage = models.ImageField(upload_to="imags" ,default="imgs/def.png") 
     def __str__(self):
        return self.user.username

class Register(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        default= 1,
        on_delete=models.CASCADE,
       
       
    )
    gender = models.CharField(choices=gender_CHOICES, max_length=10, default="MALE")
    state = models.CharField(
        choices=state_choices, max_length=100, default="Maharashtra"
    )
    cropdet = models.CharField(choices=crop_CHOICES, max_length=100, default="Peas")
    toatalLAnd = models.CharField(max_length=100)
    adress = models.TextField()
    birthdate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username

 