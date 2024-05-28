from django.db import models

class Classes(models.Model):
    id_class = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    workload = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classes'
    
    def __str__(self):
        return self.name
    