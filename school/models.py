from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class ValidityStatus(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Validity Status")
        verbose_name_plural = _("Validity Statuses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("validitystatus_detail", kwargs={"pk": self.pk})


class Country(models.Model):
    phone_code = models.CharField(_("Phone Code"), max_length=50)
    zip_code = models.CharField(_("Zip Code"), max_length=50)
    name = models.CharField(_("Country Name"), max_length=50)
    abbreviation = models.CharField(_("Abbreviation"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})


class Region(models.Model):
    country = models.ForeignKey(Country, verbose_name=_(""), on_delete=models.CASCADE)
    code = models.CharField(_("Region Code"), max_length=50)
    name = models.CharField(_("Region Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("region_detail", kwargs={"pk": self.pk})



class School(models.Model):
    code = models.CharField(_("School Code"), max_length=50)
    name = models.CharField(_("School Name"), max_length=50)
    address = models.TextField(_("Address"))
    phone_number = models.CharField(_("Phone Number"), max_length=50)
    email_address = models.EmailField(_("Email Address"), max_length=254)
    fax = models.CharField(_("Fax"), max_length=50)
    logo = models.ImageField(_("School Logo"), upload_to="photos/schools/%Y/%m/%d")
    slogan = models.CharField(_("Slogan"), max_length=50, blank=True, null=True)
    mantra = models.CharField(_("Mantra"), max_length=50, blank=True, null=True)
    nickname = models.CharField(_("Nickname"), max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.SET_NULL, null=True, default=1)
    date_of_establishment = models.DateTimeField(_("Date of Establishment"), default=timezone.now)
    description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        db_table = "school"
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school_detail", kwargs={"pk": self.pk})


class Branch(models.Model):
    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.DO_NOTHING)
    code = models.CharField(_("Branch Code"), max_length=50)
    name = models.CharField(_("Branch Name"), max_length=50)
    address = models.TextField(_("Address"))
    phone_number = models.CharField(_("Phone Number"), max_length=50)
    email_address = models.EmailField(_("Email Address"), max_length=254)
    fax = models.CharField(_("Fax"), max_length=50)
    logo = models.ImageField(_("Branch Logo"), upload_to="photos/branches/%Y/%m/%d")
    slogan = models.CharField(_("Slogan"), max_length=50, blank=True, null=True)
    mantra = models.CharField(_("Mantra"), max_length=50, blank=True, null=True)
    nickname = models.CharField(_("Nickname"), max_length=50, blank=True, null=True)
    region = models.ForeignKey(Region, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    status = models.ForeignKey(ValidityStatus, verbose_name=_("Status"), on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        db_table = "branch"
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"pk": self.pk})
