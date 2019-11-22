from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Member(models.Model):

    user = models.ForeignKey(User, verbose_name=_("user"), related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    age = models.SmallIntegerField(_("Age"))
    gender = models.CharField(_("Gender"), choices=(('male', 'Male'), ('female', 'Female')),max_length=50)
    phone_no = models.CharField(_("Phone no."), max_length=50)
    state = models.CharField(_("State"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    language_know = models.CharField(_("Languages Known"), max_length=50)
    occupation = models.CharField(_("Occupation"), max_length=50)