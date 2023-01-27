from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime
from django.contrib import admin

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
    created_at = models.DateField(_("Date Added"), auto_now_add=True)

    def __str__(self):
        return self.gender_name

    class Meta:
        db_table = 'gender'
        managed = True
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders' 

class Religion(models.Model):
    religion_name = models.CharField(_("Name of Religion"), max_length=50)
    created_at = models.DateField(_("Date Added"), auto_now_add=True)

    def __str__(self):
        return self.religion_name

    class Meta:
        db_table = 'religion'
        managed = True
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'

class BloodGroup(models.Model):
    blood_type = models.CharField(_("Blood Group Type"), max_length=50)
    description = models.TextField(_("Comment"), blank=True, null=True)

    def __str__(self):
        return self.blood_type

    class Meta:
        db_table = 'bloodgroup'
        managed = True
        verbose_name = 'BloodGroup'
        verbose_name_plural = 'BloodGroups'

class Student(models.Model):
    student_id = models.CharField(_("Student ID"), max_length=50, unique=True, default=generatestudentid)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    other_name = models.CharField(_("Other Name"), max_length=50, blank=True, null=True)
    gender = models.ForeignKey(Gender, verbose_name=_("Gender"), on_delete=models.DO_NOTHING)
    birth_date = models.DateField(_("Date of Birth"), default = timezone.now)
    residence_address = models.TextField(_("Residence Address"))
    religion = models.ForeignKey(Religion, verbose_name=_("Religion"), on_delete=models.SET_NULL, null=True)
    height = models.DecimalField(_("Height"), max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(_("Weight"), max_digits=5, decimal_places=2, blank=True, null=True)
    blood_group = models.ForeignKey(BloodGroup, verbose_name=_("Blood Group"), on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    photo = models.ImageField(_("Passport Picture"), upload_to='photos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} [{self.student_id}]'
    
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
        ordering = ['-created_at', '-first_name', 'last_name']

class AlertType(models.Model):
    alerttype_name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        self.alerttype_name

    class Meta:
        db_table = 'studentalerttype'
        managed = True
        verbose_name = 'Alert Type'
        verbose_name_plural = 'Alert Types'

class Alert(models.Model):
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    alert_type = models.ForeignKey(AlertType, verbose_name=_("Type of Alert"), on_delete=models.CASCADE)
    description = models.TextField(_("Description"))
    created_at = models.DateField(_("Date Added"), auto_now_add=True)
    alert_status = models.ForeignKey(Status, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    alert_attachment1 = models.FileField(_("Alert Attachment 1"), upload_to='files/%Y/%m/%d', max_length=100, blank=True, null=True)
    alert_attachment2 = models.FileField(_("Alert Attachment 2"), upload_to='files/%Y/%m/%d', max_length=100, blank=True, null=True)
    alert_attachment3 = models.FileField(_("Alert Attachment 3"), upload_to='files/%Y/%m/%d', max_length=100, blank=True, null=True)
    comment = models.TextField(_("Comment"), blank=True, null=True)
    
    def __str__(self):
        return f'{self.alert_description}'

    class Meta:
        db_table = 'studentalert'
        managed = True
        verbose_name = 'Alert'
        verbose_name_plural = 'Alerts'

class Hobby(models.Model):
    name = models.CharField(_("Name of Hobby"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'studenthobby'
        managed = True
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

class Guardian(models.Model):
    guardian_id = models.CharField(_("Guardian ID"), max_length=50, unique=True)
    name = models.CharField(_("Name of Guardian"), max_length=50)
    gender = models.ForeignKey(Gender, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, verbose_name=_("Students"), through='StudentGuardianAssoc')
    residence_address = models.TextField(_("Residential Address"))
    phone_number = models.CharField(_("Mobile"), max_length=50)
    occupation = models.CharField(_("Occupation"), max_length=50)
    email_address = models.EmailField(_("Email"), max_length=254)

    def __str__(self):
        self.name

    class Meta:
        db_table = 'studentguardian'
        managed = True
        verbose_name = 'Guardian'
        verbose_name_plural = 'Guardians'

class StudentGuardianRelation(models.Model):
    relationship_type = models.CharField(_("Name of Relation"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.relationship_type

    class Meta:
        db_table = 'studentguardianrelation'
        managed = True
        verbose_name = 'Student Guardian Relation'
        verbose_name_plural = 'Student Guardian Relations'

class StudentGuardianAssoc(models.Model):
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, verbose_name=_("Guardian"), on_delete=models.CASCADE)
    relation = models.ForeignKey(StudentGuardianRelation, verbose_name=_("Relation"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Date Added"), auto_now_add=True)
    description = models.TextField(_("Comment"), blank=True, null=True)

    def __str__(self):
        return f'{self.student} {self.guardian} [{self.relation}]'

    class Meta:
        db_table = 'studentguardianassoc'
        managed = True
        verbose_name = 'Student Guardian Assoc'
        verbose_name_plural = 'Student Guardian Assocs'