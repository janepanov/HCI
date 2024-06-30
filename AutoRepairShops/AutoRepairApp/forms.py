from django import forms

from .models import Repair


class RepairsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairsForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Repair
        exclude = ['user', ]