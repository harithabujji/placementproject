from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=8)

    def __str__(self):
        return self.short_name


class Course(models.Model):
    name = models.CharField(max_length=128)
    semester=models.CharField(max_length=8)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=128)
    gender = models.CharField(max_length=8)
    college = models.CharField(max_length=128)
    city= models.CharField(max_length=64)
    facebook_url = models.CharField(max_length=128)
    profile_picture=models.ImageField()

    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Marks(models.Model):
    marks= models.IntegerField()

    student= models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student {self.student.name} marks"