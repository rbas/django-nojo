# coding: utf-8
from django.http import HttpRequest

STASHED_REQUEST_KEY = '_stashed_request'

def stash_request(function):
    """
    Dekorátor pro view, který ukládá některé parametry requestu do session.

    Pokud není uživatel přihlášený a jedná se o HttpRequest uloží
    do session GET, POST, COOKIES, HTTP_REFERER, path, method.
    V session jsou data pod klíčem konstanty STASHED_REQUEST_KEY.

    nebo:

    Pokoud je uživatel přihlášený a data v session po příslušným klíčem exitují
    vyzvedne je a naimportuje do requestu.
    """
    def wrapper(request, *args, **kwargs):
        if isinstance(request, HttpRequest) and False == request.user.is_authenticated()\
            and request.session.has_key(STASHED_REQUEST_KEY) == False:
            stash = {
                'GET'         : request.GET,
                'POST'        : request.POST,
                'COOKIES'     : request.COOKIES,
                'HTTP_REFERER': request.META.get('HTTP_REFERER'),
                'path'        : request.path,
                'method'      : request.method
            }
            request.session[STASHED_REQUEST_KEY] = stash
        elif request.session.has_key(STASHED_REQUEST_KEY) and request.user.is_authenticated():
                stash = request.session.pop(STASHED_REQUEST_KEY)
                request.GET          = stash.get('GET')
                request.POST         = stash.get('POST')
                request.HTTP_REFERER = stash.get('HTTP_REFERER')
                request.path         = stash.get('path')
                request.method       = stash.get('method')

        return function(request, *args, **kwargs)
    return wrapper
