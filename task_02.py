#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

NEWFLEMISH = 'Flemish'

NEWSPANISH = inquisition.SPANISH.index('Spanish')

FLEMISH = inquisition.SPANISH[:NEWSPANISH] + NEWFLEMISH\
          + inquistition.SPANISH[NEWSPANISH+len('Spanish'):]
