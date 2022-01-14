from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
import json

from ..models import Plaza


class PlazaAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        try:
            json.loads(self.cleaned_data['permissions'])
        except ValueError as e:
            self.add_error('permissions', 'Not valid JSON: ' + str(e))
        return cleaned_data


class PlazaAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "slug",
        "description",
        "permissions",
    ]
    form = PlazaAdminForm

admin.site.register(Plaza, PlazaAdmin)
