from django.contrib import admin

# Register your models here.
# register home model
from .models import ActivityModel
admin.site.register(ActivityModel)