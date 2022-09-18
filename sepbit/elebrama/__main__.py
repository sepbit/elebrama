#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Elebrama - Eleição no Brasil para Mastodon
Copyright (C) 2020-2022 Vitor Guia

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
from sepbit.sistamapy.statuses import Statuses
from sepbit.elebrama.tse import dados_simplificados

def main():
    '''
    Entry point
    '''
    resultado = dados_simplificados(
        'https://resultados-sim.tse.jus.br/',
        'teste',
        'ele2022',
        '9238',
        'governador',
        'df',
        False
    )

    message = 'SIMULADO #eleicao #governador #df \n'
    i = 0
    for cand in resultado['cand']:
        message += cand['pvap'].strip(' ') + '% - ' + \
            cand['nm'].title()  + ' (' + str(cand['n']) + ')'

        if cand['st'] != '':
            message += ' - ' + cand['st'] + '\n'
        elif cand['dvt'] != 'Válido':
            message += ' - ' + cand['dvt'] + '\n'
        else :
            message += '\n'

        i += 1
        if i == 4:
            break

    message += '\nAtualização: ' + resultado['dt']  + ' ' + resultado['ht'] + \
        ', apuração: ' + resultado['pst'].strip() + '%' \
        '\n#bot #eleicaobr #eleicao2022'

    if resultado:
        toot = Statuses(
            environ['INSTANCE'],
            environ['TOKEN']
        )
        toot.post({
            'spoiler_text': 'Eleição para Governador DF',
            'status': message,
            'language': 'por',
            'visibility': 'public'
        })

if __name__ == '__main__':
    main()
