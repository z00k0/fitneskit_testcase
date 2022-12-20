from django.db import models


class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)
    image_url = models.URLField(blank=True)


class Integration(models.Model):
    request_id = models.UUIDField()
    club_id = models.UUIDField()
    method = models.CharField(max_length=100)
    url = models.URLField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
