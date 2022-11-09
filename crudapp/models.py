from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)+ " " + self.img

    
