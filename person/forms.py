from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Column, Layout, Row,
)
from django import forms

from person.models import (
    Person, PersonImage,
)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "JOHN WICK"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            "name"
        )


class PersonImageForm(forms.ModelForm):
    class Meta:
        model = PersonImage
        fields = "__all__"
        widgets = {
            "image": forms.ClearableFileInput(
                attrs={"multiple": False},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Row(
                Column(
                    "is_primary", css_class="form-group col-md-2 mb-0",
                ),
                Column(
                    "image", css_class="form-group col-md-10 mb-0",
                ),
            ),
        )


PersonImageFormSet = forms.models.inlineformset_factory(
    Person, PersonImage, form=PersonImageForm, can_delete=False,
    error_messages={"image": {"required": "Please provide an image"}},
    extra=0, min_num=1, validate_min=True,
)
