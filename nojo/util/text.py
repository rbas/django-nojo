# coding: utf-8
from django.utils.encoding import force_unicode
from django.utils.functional import allow_lazy

def cut_string(string, length, end_text='...'):
    """
    Ořeže HTML řetězec na určenou délku.

    Pro správné nastavení délky se musí odstranit veškeré HTML značky a entity.
    Výsledná délka zohledňujě délku proměné end_text.

    Výsledek je v unicode.

    Použití:
    >>> print(cut_string('<p>Zlat&yacute valoun</p>', 8))
    Zlatý...
    """
    string = force_unicode(string)
    from django.utils.html import strip_tags
    text = decode_entities(strip_tags(string))

    if len(text) > length:
        final_length = length - len(end_text)
        try:
            text = '%s%s' % (text[: text.rindex(' ', 0, final_length)], end_text)
        except ValueError:
            text = '%s%s' %  (text[:final_length], end_text)

    return text
cut_string = allow_lazy(cut_string, unicode)

def decode_entities(string):
    """
    Převede html entity na unicode znaky.

    Pro převod používá knihovnu BeautifulSoup

    Použití:
    >>> print(decode_entities('&yacute;'))
    ý
    """
    from BeautifulSoup import BeautifulStoneSoup
    text = unicode(BeautifulStoneSoup(string,convertEntities=BeautifulStoneSoup.HTML_ENTITIES))
    return text
decode_entities = allow_lazy(decode_entities, unicode)
