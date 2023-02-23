from django.contrib import admin
from .models import Profile,CompanyDataTable,PatentDataTable,InventorsDataTable

# Register your models here.

admin.site.register(Profile)
admin.site.register(CompanyDataTable)
admin.site.register(PatentDataTable)
admin.site.register(InventorsDataTable)
