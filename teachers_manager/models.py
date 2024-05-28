from django.db import models
from courses_manager.models import Course
from classes_manager.models import Classes


class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    register = models.IntegerField(blank=True, null=True)
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course', blank=True, null=True)
    id_class = models.ForeignKey(Classes, models.DO_NOTHING, db_column='id_class', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'
