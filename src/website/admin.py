from django.contrib import admin

# Register your models here.
from .models import Projects, Members, Contact, Event, Registration


admin.site.register(Projects)
admin.site.register(Members)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Registration)