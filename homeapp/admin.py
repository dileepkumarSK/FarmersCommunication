from django.contrib import admin
from django.contrib.auth.models import User
from .models import  Shareinformation,Personhomepage,Register
admin.site.register(Register)
admin.site.register(Shareinformation)
admin.site.register(Personhomepage)

