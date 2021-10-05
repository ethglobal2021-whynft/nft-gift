"""It should be deprecated to more advanced auth ( todo )."""
import logging

from django.http import HttpResponseRedirect
from django.urls import reverse

logger = logging.getLogger(__name__)


def session_authorization_check(function):
    def wrapper(_class, request, *args, **kwargs):
        logger.debug('check request for the session')
        if not (request.session.get('gift') and isinstance(request.session['gift'], int)):
            return HttpResponseRedirect(reverse('web:index', kwargs={}))  # todo: what is our index page

        return function(_class, request, *args, **kwargs)
    return wrapper
