from django import forms
from .models import (
    IDCard, Student,
    StudentAlert, StudentHobby,
    Guardian, StudentGuardian, 
    StudentFavoriteQuote, PreviousEducation
)

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Student
        fields = (
            'student_id', 'first_name', 'surname', 'other_name',
            'gender', 'birth_date', 'residence_address', 'phone_number',
            'email_address', 'religion', 'country', 'height', 'weight',
            'blood_group', 'photo', 'description'
        )


class GuardianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GuardianForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Guardian
        fields = (
            'guardian_id', 'title', 'name', 'gender', 'residence_address',
            'occupation', 'email_address', 'phone_number', 'photo',
            'phone_number2', 'phone_number3', 
        )
        widgets = {
            'residence_address': forms.TextInput(attrs={'class':'form-control'})
        }

class StudentGuardianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentGuardianForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = StudentGuardian
        fields = (
            'relation',
        )

class StudentHobbyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentHobbyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = StudentHobby
        fields = ("hobby",)

class PreviousEducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PreviousEducationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = PreviousEducation
        fields = ("school_name", "address", "location",)
        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control'})
        }

class StudentFavoriteQuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentFavoriteQuoteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = StudentFavoriteQuote
        fields = ("artifact", "source", "quote",)

class StudentAlertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentAlertForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = StudentAlert
        fields = ("alert_type", "description", "alert_status", "alert_attachment1",)

class IDCardForm(forms.ModelForm):
    
    class Meta:
        model = IDCard
        fields = ("idcardtype", "identity_text", "status", "expiry_date",)
