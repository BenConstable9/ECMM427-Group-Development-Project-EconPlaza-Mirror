# django imports
from django.conf import settings
from django.http import HttpResponseForbidden

# 3rd-party imports
import requests
from ipware import get_client_ip

# https://stackoverflow.com/questions/29548574/how-to-validate-google-recaptcha-v2-in-django
# https://stackoverflow.com/a/49282092
def is_recaptcha_valid(request):
    """
    Verify if the response for the Google recaptcha is valid.
    """
    return True  # Temporary
    # TODO: Setup X_FORWARDED_FROM for get_client_ip()
    # return requests.post(
    #     settings.GOOGLE_VERIFY_RECAPTCHA_URL,
    #     data={
    #         'secret': settings.RECAPTCHA_SECRET_KEY,
    #         'response': request.data.get('g-recaptcha-response'),
    #         'remoteip': get_client_ip(request)
    #     },
    #     verify=True
    # ).json().get("success", False)


def human_required(view_func):
    """
    This decorator is aimed to verify Google recaptcha in the backend side.
    """

    def wrapped(request, *args, **kwargs):
        if is_recaptcha_valid(request):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return wrapped
