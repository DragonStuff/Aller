from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Person, User

# Wizardry to create on user first login.
@receiver(post_save, sender=User)
def create_user_person(sender, instance, created, **kwargs):
    if created:
        b2 = Person.objects.create(user=instance)
        b2.save()

@receiver(post_save, sender=User)
def save_user_person(sender, instance, **kwargs):
    instance.Person.save()