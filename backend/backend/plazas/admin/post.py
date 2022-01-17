from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
import json

from ..models import Post


class PostAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        try:
            json.loads(self.cleaned_data["permissions"])
        except ValueError as e:
            self.add_error("permissions", "Not valid JSON: " + str(e))

        try:
            json.loads(self.cleaned_data["reactions"])
        except ValueError as e:
            self.add_error("reactions", "Not valid JSON: " + str(e))
        return cleaned_data


class PostAdmin(admin.ModelAdmin):
    fields = [
        "profile",
        "user",
        "plaza",
        "title",
        "content",
        "permissions",
        "reactions",
        "hidden",
        "deleted",
        "views"
    ]
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
