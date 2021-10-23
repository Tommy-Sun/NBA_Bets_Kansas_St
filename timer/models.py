from django.db import models

# Create your models here.
from datetime import date

class Timer(models.Model):

    today = models.CharField(max_length=50)
    daySinceLastUpdated = models.CharField(max_length=50)

    def __str__(self):
        return f"Hi! Today is {self.today}."

    def has_already_updated_for_the_day(self):
        self.today = date.today()
        if str(self.daySinceLastUpdated) == str(self.today):
            super().save()
            return True
        else:
            self.daySinceLastUpdated = self.today
            super().save()
            return False
        


