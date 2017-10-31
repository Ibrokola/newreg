from django.contrib import admin

from .models import AddHeader, AddCategory, Calender, DaysClosed

admin.site.register(DaysClosed)
admin.site.register(Calender)
admin.site.register(AddHeader)
admin.site.register(AddCategory)