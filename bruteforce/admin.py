from django.contrib import admin
from . import models

# Register your models here.
class BruteForceAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.BruteForceAttack, BruteForceAdmin)