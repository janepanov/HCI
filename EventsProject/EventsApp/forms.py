from django import forms

from EventsApp.models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Event
        exclude = ['user', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
