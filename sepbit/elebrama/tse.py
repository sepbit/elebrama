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

import json
import shelve
import unicodedata
from urllib.request import urlopen

def order(element):
    '''
    Organiza os candidatos por mais votados
    '''
    return int(element['seq'])

def buscar_municipio(estado, municipio):
    '''
    EA12 - Arquivo de configuração de municípios - versão 01-2020
    See https://www.tse.jus.br/eleicoes/eleicoes-2020/eleicoes-2020
        /interessados-na-divulgacao-de-resultados
    '''
    with urlopen(
        'https://resultados.tse.jus.br/oficial/ele2020/divulgacao/' \
        'oficial/426/config/mun-e000426-cm.json'
    ) as res:
        res = res.read()

    obj = json.loads(res)

    for estados in obj['abr']:
        if estados['cd'] == estado.upper():
            for municipios in estados['mu']:
                if municipio == municipios['cd']:
                    return municipios

    return False

def verificar(key, data, hora):
    '''
    Impede repetir o resultado
    '''
    with shelve.open('/tmp/elebrama', 'c') as cache:
        if cache.get(key) != data + ' ' + hora:
            cache[key] = data + ' ' + hora
            return True

    return False

def build_hashtag(title):
    '''
    Description
    '''
    adress = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore')
    return adress.decode('ASCII').title().replace(' ', '')

def resultado_consolidado(estado, municipio):
    '''
    EA04 - Arquivo de resultado consolidado - versão 01-2020
    See https://www.tse.jus.br/eleicoes/eleicoes-2020/eleicoes-2020
        /interessados-na-divulgacao-de-resultados
    '''

    with urlopen(
        'https://resultados.tse.jus.br/oficial/ele2020/divulgacao/oficial/' + \
        '426/dados-simplificados/' + estado + '/' + estado + \
        municipio + '-c0011-e000426-r.json'
    ) as res:
        res = res.read()

    obj = json.loads(res)

    if not verificar(estado + municipio, obj['dt'], obj['ht']):
        return False

    message = '#eleicao #' + \
        build_hashtag(buscar_municipio(estado, municipio)['nm']) + \
        ' - #' + estado.upper() + '\n\n'

    i = 0
    for cand in sorted(obj['cand'], key = order):
        message += cand['pvap'].strip(' ') + '% - ' + \
            cand['nm'].title()  + ' (' + str(cand['n']) + ')'

        if cand['st'] != '':
            message += ' - ' + cand['st'] + '\n'
        elif cand['dvt'] != 'Válido':
            message += ' - ' + cand['dvt'] + '\n'
        else :
            message += '\n'

        i += 1
        if i == 5:
            break

    message += '\nAtualização: ' + obj['dt']  + ' ' + obj['ht'] + \
        ', apuração: ' + obj['pst'].strip() + '%' \
        '\n#bot #eleicaobr #eleicao2020'

    return message
