from django.db import models


class CalcHistory(models.Model):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    result_number = models.IntegerField()
    date = models.DateTimeField()
