from django import forms
from .models import ArtExhibition


class ArtExhibitionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArtExhibitionForm, self).__init__(*args, *kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ArtExhibition
        fields = "__all__"
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }
