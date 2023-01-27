from django.contrib import admin
from .models import (
    Status, 
    Gender,
    Religion,
    BloodGroup,
    Student,
    AlertType,
    Alert,
    Hobby,
    Guardian,
    StudentGuardianRelation,
    StudentGuardianAssoc
)

# Register your models here.

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'description')
    list_display_links = ('status_name',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender_name', 'created_at')

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion_name', 'created_at')

@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('blood_type', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'other_name', 'last_name', 'gender', 'birth_date', 'getage', 'residence_address')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name', 'student_id')

@admin.register(AlertType)
class AlertTypeAdmin(admin.ModelAdmin):
    list_display = ('alerttype_name', 'description')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('student', 'alert_type', 'description', 'alert_status', 'created_at', 'comment')
    list_filter = ('alert_type', 'alert_status')
    search_fields = ('student',)

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('guardian_id', 'name', 'gender', 'residence_address', 'phone_number', 'occupation', 'email_address')
    search_fields = ('guardian_id', 'name', 'phone_number')

@admin.register(StudentGuardianRelation)
class StudentGuardianRelationAdmin(admin.ModelAdmin):
    list_display = ('relationship_type', 'description')

@admin.register(StudentGuardianAssoc)
class StudentGuardianAssocAdmin(admin.ModelAdmin):
    list_display = ('student', 'guardian', 'relation', 'created_at', 'description')
    search_fields = ('student', 'guardian')
    list_filter = ('relation',)