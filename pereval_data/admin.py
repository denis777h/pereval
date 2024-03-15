from django.contrib import admin

from .models import *

admin.site.register(PerevalUser)
admin.site.register(PerevalCoordinate)
admin.site.register(PerevalAdded)
admin.site.register(Image)

