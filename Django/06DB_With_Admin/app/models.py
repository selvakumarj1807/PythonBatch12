from django.db import models

# Create your models here.

class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    department_id = models.CharField(max_length=100)
   
    class Meta:  
        db_table = "tablemployee"
        
    def __str__(self):  
        return self.name
        
        
class Departments(models.Model):  
    department_id = models.CharField(max_length=100)  
    department_name = models.CharField(max_length=15) 
   