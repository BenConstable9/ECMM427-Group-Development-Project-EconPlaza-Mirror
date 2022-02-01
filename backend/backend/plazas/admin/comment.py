from django.contrib import admin
from django import forms
import json

from ..models import Comment


class CommentAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        try:
            json.loads(self.cleaned_data["reactions"])
        except ValueError as e:
            self.add_error("reactions", "Not valid JSON: " + str(e))
        return cleaned_data


class CommentAdmin(admin.ModelAdmin):
    fields = [
        "user",
        "profile",
        "post",
        "content",
        "reactions",
        "hidden",
        "deleted",
    ]
    form = CommentAdminForm


admin.site.register(Comment, CommentAdmin)
