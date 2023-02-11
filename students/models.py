from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime
from django.contrib import admin
from school.models import Branch, Country, ValidityStatus
from django.conf import settings

def generatestudentid():
    year = str(datetime.date.today().year)[2:]
    month = str(datetime.date.today().month).zfill(2)
    # last_student_id = str(Student.objects.last().id)
    # return year + month + last_student_id.zfill(6)
    try:
        last_student = Student.objects.last()
        last_student_id = last_student.id
        last_student_id += 1
    except:
        last_student_id = 1
    else:
        return int(year + month + str(last_student_id).zfill(4))

class Title(models.Model):
    name = models.CharField("Title", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'title'
        managed = True
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'


class IDCardType(models.Model):
    name = models.CharField("Name of ID Card Type", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'idcardtype'
        managed = True
        verbose_name = 'ID Card Type'
        verbose_name_plural = 'ID Card Types'

class IDCard(models.Model):
    guardian_id = models.ForeignKey("Guardian", verbose_name="Guardian", on_delete=models.CASCADE)
    idcardtype = models.ForeignKey(IDCardType, verbose_name=_("ID Card Type"), on_delete=models.CASCADE)
    identity_text = models.CharField("ID Number", max_length=50)
    expiry_date = models.DateField("Expiry Date")
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.DO_NOTHING)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.identity_text

    class Meta:
        db_table = 'idcard'
        managed = True
        verbose_name = 'ID Card'
        verbose_name_plural = 'ID Cards'

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(_("Status"), max_length=50)
    description = models.TextField(_("Status Description"), blank=True, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'status'
        managed = True
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

class Gender(models.Model):
    gender_name = models.CharField(_("Gender Name"), max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.gender_name

    class Meta:
        db_table = 'gender'
        managed = True
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders' 

class Religion(models.Model):
    religion_name = models.CharField("Name of Religion", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.religion_name

    class Meta:
        db_table = 'religion'
        managed = True
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'

class BloodGroup(models.Model):
    blood_type = models.CharField("Blood Group Type", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.blood_type

    class Meta:
        db_table = 'bloodgroup'
        managed = True
        verbose_name = 'Blood Group'
        verbose_name_plural = 'Blood Groups'

class Student(models.Model):
    student_id = models.CharField("Student ID", max_length=50, unique=True, default=generatestudentid)
    first_name = models.CharField("First Name", max_length=50)
    surname = models.CharField("Last Name", max_length=50)
    other_name = models.CharField("Other Name", max_length=50, blank=True, null=True)
    gender = models.ForeignKey(Gender, verbose_name="Gender", on_delete=models.DO_NOTHING)
    birth_date = models.DateField("Date of Birth", default = timezone.now)
    age = models.IntegerField("Age", blank=True, null=True)
    residence_address = models.TextField("Residence Address")
    phone_number = models.CharField("Phone Number", max_length=50, blank=True, null=True)
    email_address = models.EmailField("Email Address", max_length=254, blank=True, null=True)
    religion = models.ForeignKey(Religion, verbose_name="Religion", on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING, default=1)
    height = models.DecimalField("Height", max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField("Weight", max_digits=5, decimal_places=2, blank=True, null=True)
    blood_group = models.ForeignKey(BloodGroup, verbose_name="Blood Group", on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ImageField("Passport Picture", upload_to='photos/students/%Y/%m/%d', blank=True, null=True)
    branch = models.ForeignKey(Branch, verbose_name="Branch", on_delete=models.CASCADE, default=1)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.surname} '#- [{self.student_id}]'
    
    @admin.display(
        description='Age',
    )
    def getage(self):
        year = datetime.date.today().year
        return year - self.birth_date.year

    class Meta:
        db_table = 'student'
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-created_at', '-first_name', 'surname']

class AlertType(models.Model):
    alerttype_name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.alerttype_name

    class Meta:
        db_table = 'studentalerttype'
        managed = True
        verbose_name = 'Alert Type'
        verbose_name_plural = 'Alert Types'

class AlertStatus(models.Model):
    name = models.CharField("Alert Status", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    # status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'alertstatus'
        managed = True
        verbose_name = 'Alert Status'
        verbose_name_plural = 'Alert Statuses'

class StudentAlert(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    alert_type = models.ForeignKey(AlertType, verbose_name="Type of Alert", on_delete=models.CASCADE)
    alert_status = models.ForeignKey(AlertStatus, verbose_name="Alert Status", on_delete=models.SET_NULL, null=True)
    alert_attachment1 = models.FileField("Alert Attachment 1", upload_to='files/%Y/%m/%d', blank=True, null=True)
    alert_attachment2 = models.FileField("Alert Attachment 2", upload_to='files/%Y/%m/%d', blank=True, null=True)
    alert_attachment3 = models.FileField("Alert Attachment 3", upload_to='files/%Y/%m/%d', blank=True, null=True)
    comment = models.TextField("Comment", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    ending_at = models.DateTimeField("Ending Date", auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    
    def __str__(self):
        return f'{self.description}'

    class Meta:
        db_table = 'studentalert'
        managed = True
        verbose_name = 'Student Alert'
        verbose_name_plural = 'Student Alerts'

class Hobby(models.Model):
    name = models.CharField("Name of Hobby", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hobby'
        managed = True
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

class StudentHobby(models.Model):
    student = models.ForeignKey(Student, verbose_name="Name of Student", on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, verbose_name="Hobby", on_delete=models.CASCADE)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.hobby 

    class Meta:
        db_table = 'studenthobby'
        managed = True
        verbose_name = 'Student Hobby'
        verbose_name_plural = 'Student Hobbies'

class Guardian(models.Model):
    guardian_id = models.CharField("Guardian ID", max_length=50, unique=True)
    title = models.ForeignKey(Title, verbose_name="Title", on_delete=models.SET_DEFAULT, default=1)
    name = models.CharField("Name of Guardian", max_length=50)
    gender = models.ForeignKey(Gender, verbose_name="Gender", on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, verbose_name="Students", through='StudentGuardian')
    residence_address = models.TextField("Residential Address")
    occupation = models.CharField("Occupation", max_length=50)
    email_address = models.EmailField("Email", max_length=254, blank=True, null=True)
    phone_number = models.CharField("Mobile", max_length=50)
    phone_number2 = models.CharField("Mobile 2", max_length=50, blank=True, null=True)
    phone_number3 = models.CharField("Mobile 3", max_length=50, blank=True, null=True)
    # idcard = models.ForeignKey(IDCard, verbose_name="ID Card", on_delete=models.SET_NULL, null=True)
    photo = models.ImageField("Photo", upload_to="photos/guardians/%Y/%m/%d", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'guardian'
        managed = True
        verbose_name = 'Guardian'
        verbose_name_plural = 'Guardians'

class Relation(models.Model):
    relationship_type = models.CharField("Name of Relation", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.relationship_type

    class Meta:
        db_table = 'relation'
        managed = True
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'

class StudentGuardian(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, verbose_name="Guardian", on_delete=models.CASCADE)
    relation = models.ForeignKey(Relation, verbose_name="Relation", on_delete=models.CASCADE)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.student} {self.guardian} [{self.relation}]'

    class Meta:
        db_table = 'studentguardian'
        managed = True
        verbose_name = 'Student Guardian '
        verbose_name_plural = 'Student Guardians'


class QuoteSource(models.Model):
    name = models.CharField("Name of Source", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'quotesource'
        managed = True
        verbose_name = 'Quote Source'
        verbose_name_plural = 'Quote Sources'


class QuoteArtifact(models.Model):
    name = models.CharField("Name of Source", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'quoteartifact'
        managed = True
        verbose_name = 'Quote Artifact'
        verbose_name_plural = 'Quote Artifacts'


class StudentFavoriteQuote(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    artifact = models.ForeignKey(QuoteArtifact, verbose_name="What is the quote about?", on_delete=models.SET_NULL, null=True)
    source = models.ForeignKey(QuoteSource, verbose_name="Where did you know it from?", on_delete=models.SET_NULL, null=True)
    quote = models.TextField("Quote")
    comment = models.TextField("Comment", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.quote

    class Meta:
        db_table = 'studentfavoritequote'
        managed = True
        verbose_name = 'Student Favorite Quote'
        verbose_name_plural = 'Student Favorite Quotes'


class PreviousEducation(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    school_name = models.CharField("Name of School", max_length=50)
    address = models.TextField("Address", blank=True, null=True)
    location = models.CharField("Location", max_length=50, blank=True, null=True)
    comment = models.TextField("Comment", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    last_report = models.FileField("Last Report", upload_to="files/students_reports_from_previous_school/%Y/%m/%d")
    
    def __str__(self):
        return self.school_name

    class Meta:
        db_table = 'previouseducation'
        managed = True
        verbose_name = 'Previous Education'
        verbose_name_plural = 'Previous Educations'