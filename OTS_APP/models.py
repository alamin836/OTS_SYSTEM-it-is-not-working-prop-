from django.db import models

class Candidate(models.Model):
    Username=models.CharField(primary_key=True,max_length=255)
    Password=models.CharField(null=False,max_length=255)
    Name=models.CharField(null=False,max_length=255)
    Test_attempt=models.IntegerField(default=0)
    Points=models.FloatField(default=0)
    def __str__(self):
        return self.Name
class Question(models.Model):
    Queid=models.BigAutoField(primary_key=True,auto_created=True)
    Que=models.TextField()
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    Ans=models.CharField(max_length=2)
  
class Result(models.Model):
    Resultid=models.BigAutoField(primary_key=True,auto_created=True)
    Username=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attempt=models.IntegerField()
    Right=models.IntegerField()
    Wrong=models.IntegerField()
    points=models.FloatField()
 




