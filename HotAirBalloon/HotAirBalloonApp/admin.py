from django.contrib import admin

from HotAirBalloonApp.models import HotAirBalloon, Airline, Pilot, AirlinePilot, Flight


# Register your models here.

class AirlinePilotAdmin(admin.ModelAdmin):
    pass
class AirlinePilotInlineAdmin(admin.TabularInline):
    model = AirlinePilot
    extra = 1

class HotAirBalloonAdmin(admin.ModelAdmin):
    pass

class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [AirlinePilotInlineAdmin, ]

class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "surname",)



class FlightAdmin(admin.ModelAdmin):
    exclude = ("user", )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HotAirBalloon, HotAirBalloonAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(AirlinePilot, AirlinePilotAdmin)