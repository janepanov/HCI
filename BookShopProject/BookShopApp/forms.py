from django import forms
from .models import Book, Author, BookAuthor


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }

