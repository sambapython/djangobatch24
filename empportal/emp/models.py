from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_type_choices =[('ADMIN','ADMIN'),('HR','HR'),('EMPLOYEE','EMPLOYEE')]
    empid = models.CharField(max_length=15, unique=True)#varchar
    name = models.CharField(max_length=250)
    address=models.CharField(max_length=600, null=True, blank=True)
    salary_perday = models.PositiveIntegerField(blank=True)
    emp_type = models.CharField(choices=emp_type_choices, max_length=10) 
    email = models.EmailField(max_length=250, blank=True)
    phone = models.CharField(max_length=15, null=True)



