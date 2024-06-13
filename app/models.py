from django.db import models

# Create your models here.
class School(models.Model):
    sname = models.CharField(max_length=50)
    sprincipal = models.CharField(max_length=50)

    def __str__(self):
        return self.sname
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name='students')
    phno = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    

    