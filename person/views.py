from django.views.generic import (
    CreateView, DetailView, UpdateView,
)

from person.forms import (
    PersonForm,
    PersonImageFormSet,
)
from person.models import (
    Person,
)


# Create your views here.
class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "person/person_form.html"

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["images"] = PersonImageFormSet(self.request.POST, self.request.FILES)
        else:
            context["images"] = PersonImageFormSet()
        # print(f"PersonCreateView.get_context_data: {context}")
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        # print(f"PersonCreateView.form_valid: {context}")
        images = context["images"]
        if images.is_valid():
            self.object = form.save()
            # print(f"PersonCreateView.form_valid.FILES: {self.request.FILES}")
            for v in self.request.FILES.values():
                self.object.person_image.create(image=v)
        else:
            # print(f"PersonCreateView.form_valid not all are valid: {form.errors}")
            return self.form_invalid(form)
        return super(PersonCreateView, self).form_valid(form)


class PersonDetailView(DetailView):
    model = Person
    context_object_name = "personQS"


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["images"] = PersonImageFormSet(
                self.request.POST, self.request.FILES, instance=self.object,
            )
        else:
            context["images"] = PersonImageFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        # print(f"PersonUpdateView.form_valid: {context}")
        images = context["images"]
        if images.is_valid():
            self.object = form.save()
            print(f"PersonUpdateView.form_valid.FILES: {self.request.FILES}")
            for v in self.request.FILES.values():
                self.object.person_image.create(image=v)
        else:
            print(f"PersonUpdateView.form_valid not all are valid: {form.errors}")
            return self.form_invalid(form)
        return super(PersonUpdateView, self).form_valid(form)
