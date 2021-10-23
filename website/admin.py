from django.contrib import admin
from better.models import NbaBetter
from better.models import Teams
from timer.models import Timer

admin.site.register(NbaBetter)
admin.site.register(Teams)
admin.site.register(Timer)

