from django.db import models

# Create your models here.


class Grade(models.Model):
    g_name = models.CharField(max_length=10)


    class Meta:
        db_table = 'grade'