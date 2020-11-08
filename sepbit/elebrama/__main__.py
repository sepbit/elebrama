#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Elebrama - Eleição no Brasil para Mastodon
Copyright (C) 2020 Vitor Guia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import sys
from os import environ
from sepbit.elebrama.mastodon import statuses
from sepbit.elebrama.tse import resultado_consolidado, buscar_municipio


def main():
    '''
    Entry point
    '''
    resultado = resultado_consolidado(sys.argv[1], sys.argv[2])

    if resultado:
        statuses(
            environ['INSTANCE'],
            environ['TOKEN'],
            data = {
                'spoiler_text': 'Atualização eleição ' +\
                    buscar_municipio(sys.argv[1], sys.argv[2])['nm'].title() + \
                    ' - ' + sys.argv[1].upper(),
                'status': resultado,
                'language': 'por',
                'visibility': 'public'
            }
        )


if __name__ == '__main__':
    main()
