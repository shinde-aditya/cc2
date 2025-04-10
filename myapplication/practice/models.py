from django.db import models

# Create your models here.
class Students(models.Model):
    Roll_no = models.IntegerField()
    studentName = models.CharField(max_length=100)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    math = models.IntegerField()


class Teachers(models.Model):
    teacher_id=models.IntegerField()
    teacher_name=models.CharField(max_length=100)
    teacher_mobile=models.IntegerField()

class Contacts1(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()








 