from django.contrib import admin

# Register your models here.
from .models import Projects, Members, Contact


admin.site.register(Projects)
admin.site.register(Members)
admin.site.register(Contact)