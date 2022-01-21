from django.contrib import admin
from .models import MyPizza, MyTopping


admin.site.register(MyPizza)
admin.site.register(MyTopping)
