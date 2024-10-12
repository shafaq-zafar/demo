from django.contrib import admin
from service.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(Contact, ContactAdmin)  # Register Service model with ContactAdmin class
    


# Register your models here.
