from django.db import models
from django.utils import timezone

class Weight(models.Model):
    weight = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def add_weight(self):
        self.date = timezone.now()
        self.save()
