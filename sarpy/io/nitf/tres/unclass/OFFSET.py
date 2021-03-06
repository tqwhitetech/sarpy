# -*- coding: utf-8 -*-

from ..tre_elements import TREExtension, TREElement

__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class OFFSETType(TREElement):
    def __init__(self, value):
        super(OFFSETType, self).__init__()
        self.add_field('LINE', 'd', 8, value)
        self.add_field('SAMPLE', 'd', 8, value)


class OFFSET(TREExtension):
    _tag_value = 'OFFSET'
    _data_type = OFFSETType
