from django.contrib import admin
from visitors.models import Visitor
# Register your models here.


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass
