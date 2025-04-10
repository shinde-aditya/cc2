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






#     from django.db import models

# # Create your models here.
# class Students(models.Model):
#     Roll_no=models.models.IntegerField()
#     studentName=models.name = models.CharField(max_length=100)
#     physics=models.models.IntegerField()
#     chemistry=models.models.IntegerField()
#     math=models.models.IntegerField()