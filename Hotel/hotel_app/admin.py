from django.contrib import admin

from hotel_app.forms import RoomEmployeeForm
from hotel_app.models import RoomEmployee, Room, Employee, Reservation


# Register your models here.


class RoomEmployeeAdmin(admin.ModelAdmin):
    pass


class RoomEmployeeInline(admin.StackedInline):
    model = RoomEmployee
    extra = 1
    form = RoomEmployeeForm


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomEmployeeInline, ]
    list_display = ('room_number', 'is_clean',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        emp = Employee.objects.filter(user=request.user,employee_type='H').first()
        if obj and emp:
            return True


class EmployeeAdmin(admin.ModelAdmin):
    pass


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('code', 'room',)
    exclude = ('user', )

    def save_model(self, request, obj, form, change):
        if obj.room.is_clean:
            obj.user = request.user
            return super(ReservationAdmin, self).save_model(request, obj, form, change)
        return False

    def has_change_permission(self, request, obj=None):
        recept = Employee.objects.filter(user=request.user, employee_type='R').first()
        manag = Employee.objects.filter(user=request.user, employee_type='M').first()
        if obj and (obj.user == request.user or recept or manag):
            return True

#        if obj and (obj.user == request.user or obj.confirmed_by.employee_type.__eq__('M')
#                    or obj.confirmed_by.employee_type.__eq__('R')):
#            return True


admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(RoomEmployee, RoomEmployeeAdmin)
