from django.db import models

# Create your models here.
import time

class Timer():
    seconds = time.time()
    local_time = time.localtime(seconds)
    today = [local_time.tm_mday]
    daySinceLastUpdated = []


    def has_already_updated_for_the_day(self):
        if self.daySinceLastUpdated == self.today:
            return True
        else:
            self.daySinceLastUpdated = self.today
            return False

