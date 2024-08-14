from django.db import models

# Create your models here.


class sexo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(
        max_length=100,
        null=False,
        blank=False
    )