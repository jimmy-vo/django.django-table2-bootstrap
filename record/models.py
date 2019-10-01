from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("country_detail", args=(self.pk,))

    @property
    def summary(self):
        return "%s (pop. %s)" % (self.name, self.population)


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="full name")
    height = models.DecimalField(max_digits=10, decimal_places=2, default=1.65)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person_detail", args=(self.pk,))
