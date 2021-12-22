from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

# Taken from: https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin
fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('banned', 'verified')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
