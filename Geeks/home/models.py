from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=40)
    content=models.TextField()

    def __str__(self):
        return "This is from "+ self.name+' - '+self.email
    
    