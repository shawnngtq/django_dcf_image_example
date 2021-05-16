from django.contrib import admin
from django.db.models import (
    ManyToManyField, ManyToManyRel, ManyToOneRel,
)

from person.forms import (
    PersonForm, PersonImageForm,
)
from person.models import (
    Person, PersonImage,
)


# Register your models here.
class PersonImageAdmin(admin.ModelAdmin):
    form = PersonImageForm
    list_display = [
        field.name for field in PersonImage._meta.get_fields()
        if not isinstance(field, (ManyToManyField,))
    ]
    list_per_page = 20
    search_fields = ["person__display_name"]


admin.site.register(PersonImage, PersonImageAdmin)


class PersonImageInline(admin.TabularInline):
    model = PersonImage
    extra = 0
    form = PersonImageForm
    min_num = 1
    validate_min = True


class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = [
        field.name for field in Person._meta.get_fields()
        if isinstance(field, (ManyToManyField,))
    ]
    form = PersonForm
    inlines = [PersonImageInline]
    list_display = [
        field.name for field in Person._meta.get_fields()
        if not isinstance(field, (ManyToManyField, ManyToManyRel, ManyToOneRel,))
    ]
    list_per_page = 20
    search_fields = ["name"]


admin.site.register(Person, PersonAdmin)
