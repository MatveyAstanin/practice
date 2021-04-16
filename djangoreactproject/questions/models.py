from django.contrib.postgres.fields import ArrayField
from django.db import models


class Questions(models.Model):
    id = models.AutoField(primary_key=True )
    title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True)


    def __str__(self):
        return self.title

# Create your models here.
