from django.db.models.signals import post_save
from .models import School, Branch, Region, ValidityStatus
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from users.models import CustomUser

default_region = Region.objects.first()
default_user = CustomUser.objects.first()
default_status = ValidityStatus.objects.first()

@receiver(post_save, sender = School)
def create_school_branch(sender, instance, created, **kwargs):
    if created:
        Branch.objects.create(school=instance, code=instance.code, 
            name=instance.name,
            address=instance.address,
            phone_number=instance.phone_number,
            email_address = instance.email_address,
            fax=instance.fax,
            logo = instance.logo,
            slogan=instance.slogan,
            mantra = instance.mantra,
            nickname = instance.nickname,
            created_by = default_user,
            region = default_region,
            status = default_status,
            description = '',
            created_at = timezone.now,

        )

# @receiver(post_save, sender = School)
# def create_school_branch(sender, instance, created, **kwargs):
#     instance.branch.save()