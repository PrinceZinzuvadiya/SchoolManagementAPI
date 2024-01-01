from django.db import models

class principal(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    salary=models.IntegerField()
    attendance=models.CharField(max_length=20)

class faculty(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    salary=models.IntegerField()
    subject=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)

class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    city=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)
    feespending=models.CharField(max_length=20)
    remarks=models.CharField(max_length=100)