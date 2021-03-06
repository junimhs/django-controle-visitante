from django.contrib import admin

# Register your models here.
from gatekeepers.models import Gatekeeper


@admin.register(Gatekeeper)
class GateKeeperAdmin(admin.ModelAdmin):
    pass
