from django.contrib import admin
from .models import Vender, Purchase, Historical

# Register your models here.
admin.site.register([Vender, Purchase, Historical])
