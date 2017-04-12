from django.db import models
from django.utils import timezone
import datetime

class Weight(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    weight = models.FloatField()
    date = models.DateField("Date", default=datetime.date.today)

    def add_weight(self):
        self.date = datetime.date.today()
        self.save()
