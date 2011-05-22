# coding: utf-8
from django.test import TestCase
from django.template import Template, Context, loader

class TemplateTagTestCase(TestCase):
    """
    Slouží pro testování template tagů.

    Test se používá porovnáním výstupu z tagu a výstupu z šablony.
    Pro získání těchto výstupů jsou připraveny metody render_tag a render_template.

    Při používání metody render_tag je potřeba nastavit vlastnost tag_library ve které musí být
    název knihovny tagů.
    """
    tag_library = '',

    def render_tag(self, tag_name = '', context = {}):
        """
        Vyrenderuje tag z knihovny a vrátí výstup.
        """
        # Řetězec je schválně spojován ručně a né pomocí fomátování stringů. (string obsahuje klíčový znak %)
        template = '{% load ' +  self.tag_library + '%}{% ' + tag_name + '%}'
        t = Template(template)
        c = Context(context)
        return t.render(c)

    def render_template(self, template_name='', context={}):
        """
        Vyrenderuje šablonu a vrátí její výstup.
        """
        t = loader.get_template(template_name);
        c = Context(context)
        return t.render(c)
