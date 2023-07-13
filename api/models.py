from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField( max_length=50)
    id_no=models.CharField( max_length=50)
    branch=models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.name