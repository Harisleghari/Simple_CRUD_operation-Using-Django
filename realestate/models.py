from django.db import models


class Employee(models.Model):
    eid = models.CharField(max_length=20, default='DEFAULT VALUE')
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    email = models.EmailField()
    contact = models.CharField(max_length=10, default='DEFAULT VALUE')

    class Meta:
        db_table = "employee"
