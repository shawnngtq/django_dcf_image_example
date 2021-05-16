from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField


# Create your models here.
class Person(models.Model):
    name = models.TextField()

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person-detail", args=[str(self.id)])


class PersonImage(models.Model):
    person = models.ForeignKey(
        Person, null=True, on_delete=models.SET_NULL, related_name="person_image",
    )
    image = ProcessedImageField(
        format="WEBP", upload_to='',
    )
    is_primary = models.BooleanField(
        default=False, help_text="Tick if this is primary image",
    )

    class Meta:
        db_table = "person_image"

    def __str__(self):
        return str(self.image)
