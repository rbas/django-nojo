# coding: utf-8

from django.conf import settings
from django.contrib.admin.options import BaseModelAdmin
from django.db.models.fields import Field

from tinymce.widgets import TinyMCE


class TinyMCEAdminMixin(object):
    """
    Přidá TinyMCE editor k vybraným prvkům.
    """

    html_fields = {
        'content' : {'attrs': {'cols': 80, 'rows': 50}},
        'perex'   : {'attrs': {'cols': 80, 'rows': 10}},
    }

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Zavolá pro definované prvky metodu formfield_for_htmlfield
        """
        assert isinstance(self, BaseModelAdmin)
        if db_field.name in self.html_fields:
            attrs = self.html_fields[db_field.name]
            return self.formfield_for_htmlfield(db_field, **attrs)
        return super(TinyMCEAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)

    def formfield_for_htmlfield(self, db_field, **kwargs):
        """
        Přidá prvku widget TinyMCE
        """
        assert isinstance(db_field, Field)
        return db_field.formfield(widget=TinyMCE(**kwargs))

    class Media:
        js = (settings.TINYMCE_JS_URL,)
