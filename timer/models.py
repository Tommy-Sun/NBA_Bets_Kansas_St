from django.db import models

# Create your models here.
from datetime import date

class Timer():

    def __init__(self):
        self.today = date.today()
        self.daySinceLastUpdated = self.today


    def has_already_updated_for_the_day(self):
        self.today = date.today()
        if self.daySinceLastUpdated == self.today:
            return True
        else:
            self.daySinceLastUpdated = self.today
            return False

