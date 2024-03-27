from django.contrib import admin
from .models import MCQ, NUMERICAL


# Register your models here.
class MCQAdmin(admin.ModelAdmin):
    list_display = ('EXC', 'SUB', 'QN', 'QA')

admin.site.register(MCQ, MCQAdmin)

class NUMERICALAdmin(admin.ModelAdmin):
    list_display = ('EXC', 'SUB', 'QNN', 'QA')

admin.site.register(NUMERICAL, NUMERICALAdmin)

