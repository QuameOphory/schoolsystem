from django.contrib import admin
from .models import Country, Region, School, Branch, ValidityStatus

# Register your models here.
@admin.register(ValidityStatus)
class ValidityStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'country_name', 'zip_code', 'phone_code', 'created_by', 'created_at')

@admin.register(Region)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'country', 'created_by', 'created_at')
    list_filter = ('country',)
    search_fields = ('country', 'name', 'code')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'address', 'phone_number', 'email_address', 'fax', 'country', 'date_of_establishment')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'address', 'phone_number', 'email_address', 'fax', 'nickname', 'created_by', 'created_at')