from django.contrib import admin

from EventsApp.models import BandEvent, Event, Band


# Register your models here.

class BandEventInline(admin.TabularInline):
    model = BandEvent
    extra = 1


class BandEventAdmin(admin.ModelAdmin):
    pass


class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', ]
    pass


class EventAdmin(admin.ModelAdmin):
    inlines = [BandEventInline, ]
    list_display = ['name', 'date', ]
    exclude = ['user', 'bands',]

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


admin.site.register(Event, EventAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(BandEvent, BandEventAdmin)
