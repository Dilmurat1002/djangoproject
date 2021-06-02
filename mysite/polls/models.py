from django.db import models

class Positions(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    characteristics = models.CharField(max_length=100)
    positions = models.OneToOneField(Positions, on_delete=models.DO_NOTHING)
    project = models.ManyToManyField("Project")

class Salary(models.Model):
    amount = models.FloatField(max_length=50)
    start_date = models.DateTimeField(max_length=50)
    end_date = models.DateTimeField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(max_length=50)
    end_date = models.DateTimeField(max_length=50)

