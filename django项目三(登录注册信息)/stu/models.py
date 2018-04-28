from django.db import models

# Create your models here.

class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'day51_student'


class StudentInfo(models.Model):

    s_age = models.CharField(max_length=3)
    s_addr = models.CharField(max_length=20)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'stu_info'