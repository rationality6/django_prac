from django.db import models


class Used_market(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Random_number(models.Model):
    num = models.IntegerField()
