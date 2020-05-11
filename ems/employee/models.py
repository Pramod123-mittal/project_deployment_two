from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this process of ist line is called the exetending of use(existing model)
    designation = models.CharField(max_length=35, null=False, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%y/%m/%d/', null=True, blank=True)

    # width_field='picture_width',height_field='picture_height',
    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)


# learning proxy model
# fields are not allowed in proxy models we can add property to existing models
# multiple inheritence is also not allowed
# we are adding properties to User class bu using this class
# proxy models based on inheritence
class Employee(User):
    class Meta:
        ordering = ("username",)
        proxy = True




@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    else:
        instance.profile.save()
