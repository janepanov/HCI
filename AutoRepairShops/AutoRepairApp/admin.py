from django.contrib import admin

from .models import Manufacturer, Car, WorkShop, Repair, ManufacturerWorkshop

# Register your models here.

class WorkshopInLineAdmin(admin.TabularInline):
    model = ManufacturerWorkshop
    extra = 1

class WorkshopAdmin (admin.ModelAdmin):
    inlines = [WorkshopInLineAdmin, ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class RepairAdmin (admin.ModelAdmin):
    exclude = ("user", )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RepairAdmin, self).save_model(request, obj, form, change)

class CarAdmin (admin.ModelAdmin):
    list_display = ("type", "max_speed", )

class ManufacturerAdmin (admin.ModelAdmin):
    list_display = ("name", )

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class ManufacturerWorkshopAdmin (admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(WorkShop, WorkshopAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(ManufacturerWorkshop, ManufacturerWorkshopAdmin)