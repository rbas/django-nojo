# coding: utf-8
from datetime import datetime
from django.db import models

OBJECT_STATUS_DELETED   = -1
OBJECT_STATUS_DRAFT     =  0
OBJECT_STATUS_PUBLISHED =  1

OBJECT_STATUSES = (
    [OBJECT_STATUS_DELETED,   u'Smazaný'],
    [OBJECT_STATUS_DRAFT,     u'Rozepsaný'],
    [OBJECT_STATUS_PUBLISHED, u'Publikovaný']
)

class PublishedManager(models.Manager):
    """
    Manager pro objekty pracující se statusy publikování.
    """

    def published(self, *args, **kwargs):
        """
        Filtruje pouze publikované objekty.
        """
        kwargs['status'] = OBJECT_STATUS_PUBLISHED
        return self.all().filter(*args, **kwargs)

    def latest_items(self, *args, **kwargs):
        """
        Vrátí publikované objekty řazené podle data publikování.
        """
        return self.published(*args, **kwargs).order_by('-published')

    def publish_scheduled(self, time_from=None):
        """
        Nastavý publikovaný status položkám předaného manageru.
        """
        unpublished = self.all().filter(status=OBJECT_STATUS_DRAFT,
                                    published__lte=datetime.now())
        if time_from:
            unpublished.filter(published__gt=time_from)

        for item in unpublished:
            item.status = OBJECT_STATUS_PUBLISHED
            item.save()

def published_pre_save_handler(sender, **kwargs):
    """
    Handler nastavuje objektu časy změn.

    Pokud se ukládá nový objekt nastaví se mu vlastnost created na aktuální čas.
    Pokud se ukládá již existující objekt a hodnota published je menší
    než aktuální čas, nastaví se vlastnost updated na akuální čas.
    """
    try:
        model = kwargs.get('instance')
        now = datetime.now()

        if not model.id:
        # Pokud objekt ještě nebyl vytvořen nastavíme aktuální čas.
            if hasattr(model, 'created'):
                model.created = now
                model.updated = None
        elif model.id and model.published < now:
        # Pokud objekt není nový a je publikovaný nastavíme čas úprav.
            model.updated = now
    except Exception, e:
        from django.conf import settings
        if settings.DEBUG:
            import warnings
            warnings.warn(u'V signalu "published_pre_save_handler" doslo k chybe. %s', e)
