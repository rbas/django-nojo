# coding: utf-8
import unittest

from nojo.test.decorators import data_provider
from nojo.util.text import cut_string, decode_entities

class TestTextFunctions(unittest.TestCase):

    testing_data_for_cut_string = (
        ( u'Zlatý...', (u'<p>Zlat&yacute; valoun</p>', 8)),
        ( u'Zlatý@@@', (u'<p>Zlatý valoun</p>', 8, '@@@')),
        ( u'Zlatý valoun', (u'<p>Zlat&yacute; valoun</p>', 12)),
        ( u'Zlatý valoun', (u'<p>Zlatý valoun</p>', 12)),
    )

    testing_data_for_decode_entities = (
        (u'Frantisek\xa0je\xa0dobrý.', (u'Frantisek&nbsp;je&nbsp;dobrý.')),
        (u'ý', (u'&yacute;')),
    )

    @data_provider(testing_data_for_cut_string)
    def test_cut_string(self, result, *args):
        args = args[0]
        self.assertEquals(result, cut_string(*args))

    @data_provider(testing_data_for_decode_entities)
    def test_decode_entities(self, result, *args):
        self.assertEquals(result, decode_entities(args[0]))
