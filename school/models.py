from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class ValidityStatus(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Created By"), on_delete=models.CASCADE)

    class Meta:
        verbose_name ="Validity Status"
        verbose_name_plural ="Validity Statuses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("validitystatus_detail", kwargs={"pk": self.pk})


class Country(models.Model):
    phone_code = models.CharField("Phone Code", max_length=50)
    zip_code = models.CharField("Zip Code", max_length=50)
    country_name = models.CharField("Country Name", max_length=50)
    abbreviation = models.CharField("Abbreviation", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})


class Region(models.Model):
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.CASCADE)
    code = models.CharField("Region Code", max_length=50)
    name = models.CharField("Region Name", max_length=50)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("region_detail", kwargs={"pk": self.pk})



class School(models.Model):
    code = models.CharField("School Code", max_length=50)
    name = models.CharField("School Name", max_length=50)
    address = models.TextField("Address")
    phone_number = models.CharField("Phone Number", max_length=50)
    email_address = models.EmailField("Email Address", max_length=254)
    fax = models.CharField("Fax", max_length=50)
    logo = models.ImageField("School Logo", upload_to="photos/schools/%Y/%m/%d")
    slogan = models.CharField("Slogan", max_length=50, blank=True, null=True)
    mantra = models.CharField("Mantra", max_length=50, blank=True, null=True)
    nickname = models.CharField("Nickname", max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.SET_NULL, null=True, default=1)
    date_of_establishment = models.DateTimeField("Date of Establishment", default=timezone.now)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE)

    class Meta:
        db_table = "school"
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school_detail", kwargs={"pk": self.pk})


class Branch(models.Model):
    school = models.ForeignKey(School, verbose_name="School", on_delete=models.DO_NOTHING)
    code = models.CharField("Branch Code", max_length=50)
    name = models.CharField("Branch Name", max_length=50)
    address = models.TextField("Address")
    phone_number = models.CharField("Phone Number", max_length=50)
    email_address = models.EmailField("Email Address", max_length=254)
    fax = models.CharField("Fax", max_length=50)
    logo = models.ImageField("Branch Logo", upload_to="photos/branches/%Y/%m/%d")
    slogan = models.CharField("Slogan", max_length=50, blank=True, null=True)
    mantra = models.CharField("Mantra", max_length=50, blank=True, null=True)
    nickname = models.CharField("Nickname", max_length=50, blank=True, null=True)
    region = models.ForeignKey(Region, verbose_name="Region", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name="Status", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Created By", on_delete=models.CASCADE)

    class Meta:
        db_table = "branch"
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"pk": self.pk})
