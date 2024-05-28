from django.db import models
from classes_manager.models import Classes

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    id_class = models.ForeignKey(Classes, models.DO_NOTHING, db_column='id_class', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'

    def __str__(self):
        return self.name

