from django.contrib import admin

from receipt import models

admin.site.register(models.Company)
admin.site.register(models.Establishment)
admin.site.register(models.Receipt)
admin.site.register(models.Tag)
