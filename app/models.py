from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    percentage=models.IntegerField()
    remarks=models.CharField(max_length=4)

    def __str__(self) -> str:
        return str(self.sid)
    

class Course(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    cid=models.IntegerField()
    Course=models.CharField(max_length=100)
    college=models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.cid)
    