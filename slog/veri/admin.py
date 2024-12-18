from django.contrib import admin
from .models import CustomUser,backuser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(backuser)
