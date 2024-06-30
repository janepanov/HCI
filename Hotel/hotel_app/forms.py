from django import forms
from .models import Reservation, RoomEmployee, Employee


class RoomEmployeeForm(forms.ModelForm):
    class Meta:
        model = RoomEmployee
        fields = ['room', 'employee']

    def __init__(self, *args, **kwargs):
        super(RoomEmployeeForm, self).__init__(*args, **kwargs)
        # Filter the employee queryset to only include employees of type 'H'
        self.fields['employee'].queryset = Employee.objects.filter(employee_type='H')

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Reservation
        exclude = ["user", ]
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }
