from django.contrib import admin
from .models import Part

class PartAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)

admin.site.register(Part, PartAdmin)


