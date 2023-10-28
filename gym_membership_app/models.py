from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Membership(models.Model):
    sessions_status = (
        (1, ('12 sessions in month')),
        (2, ('16 sessions in month')),
        (3, ('30 sessions in month')),
    )
    GYM = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    sessions = models.PositiveSmallIntegerField(choices=sessions_status, default=1, null=True)
    membership_date = models.DateField(null=True)
    membership_remain = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
