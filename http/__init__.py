# coding: utf-8
from django.http import HttpResponseRedirect, HttpRequest

def sanitizeHttpReferer(request, alternativeUrl):
    """
    Pokud referef není z hostu v requestu použije se alternativeUrl.
    """
    import re
    referer = request.META.get('HTTP_REFERER', '')

    current_uri = '%s://%s' % (request.is_secure() and 'https' or 'http', request.get_host())
    host_pattern = re.compile(r'(' + current_uri + ')')

    if not re.match(host_pattern, referer):
        referer = alternativeUrl

    return referer

def httpResponseBack(request, alternativeUrl='/'):
    """
    Přesměruje http požadavek zpět.

    Pokud sanitizer shleda referef za vadny vrati alternativni url.

    @uses  sanitizeHttpReferer
    @raise ValueError          Pokud parametr není instancí django.http.HttpRequest
    """
    if False == isinstance(request, HttpRequest):
        raise ValueError(u'Parametr "request" musí být instancí "django.http.HttpRequest"');

    backUrl = sanitizeHttpReferer(request, alternativeUrl) or alternativeUrl
    return HttpResponseRedirect(backUrl)
