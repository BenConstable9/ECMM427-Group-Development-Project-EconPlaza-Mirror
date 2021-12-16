from rest_framework.permissions import AllowAny

# Taken form https://stackoverflow.com/questions/39392007/django-rest-framework-viewset-permissions-create-without-list

class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False
