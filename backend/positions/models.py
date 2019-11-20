from django.db import models

class Position(models.Model):
    techType = models.CharField(max_length=200)
    annualPay = models.CharField(max_length=200)
    recruitGroup = models.CharField(max_length=200)
    candidateCriteria = models.CharField(max_length=200)
    recruitDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.techType +"  " + self.candidateCriteria