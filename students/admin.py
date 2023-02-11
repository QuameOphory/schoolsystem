from django.contrib import admin
from .models import (
    Title, IDCardType, IDCard, Gender, Religion, BloodGroup, Student,
    AlertType, AlertStatus, StudentAlert, Hobby, StudentHobby,
    Guardian, Relation, StudentGuardian, QuoteArtifact, 
    QuoteSource, StudentFavoriteQuote, PreviousEducation
)
# from .models import

@admin.register(IDCardType)
class IDCardTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(IDCard)
class IDCardAdmin(admin.ModelAdmin):
    list_display = ('idcardtype', 'identity_text', 'expiry_date', 'status')
    search_fields = ('idcardtype', 'identity_text')
    list_filter = ('status',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender_name',)

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion_name',)

@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('blood_type',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'other_name', 'surname', 'gender', 'birth_date', 'residence_address', 'phone_number', 'email_address', 'religion', 'country')
    search_fields = ('student', 'first_name')
    list_filter = ('branch', )

@admin.register(AlertType)
class AlertTypeAdmin(admin.ModelAdmin):
    list_display = ('alerttype_name',)

@admin.register(AlertStatus)
class AlertStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(StudentAlert)
class StudentAlertAdmin(admin.ModelAdmin):
    list_display = ('student', 'alert_type', 'alert_status', 'description')
    search_fields = ('student', )
    list_filter = ('alert_type', 'alert_status')

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(StudentHobby)
class StudentHobbyAdmin(admin.ModelAdmin):
    list_display = ('student', 'hobby')
    search_fields = ('student',)

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('guardian_id', 'title', 'name', 'residence_address', 'occupation', 'email_address', 'phone_number')
    search_fields = ('guardian_id', 'name')

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('relationship_type', )

@admin.register(StudentGuardian)
class StudentGuardianAdmin(admin.ModelAdmin):
    list_display = ('student', 'guardian', 'relation')
    search_fields = ('student', )

@admin.register(QuoteSource)
class QuoteSourceAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(QuoteArtifact)
class QuoteArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(StudentFavoriteQuote)
class StudentFavoriteQuoteAdmin(admin.ModelAdmin):
    list_display = ('student', 'artifact', 'source', 'quote')
    search_fields = ('student', )
    list_filter = ('artifact',)


@admin.register(PreviousEducation)
class PreviousEducationAdmin(admin.ModelAdmin):
    list_display = ('student', 'school_name', 'address')
    search_fields = ('student', 'school_name')