from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    register = models.IntegerField(null=False, blank=False)
    course = models.IntegerField(null=False, blank=False)
    classes = models.IntegerField(null=False, blank=False)
