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

import json
import shelve
import unicodedata
from urllib.request import urlopen

def get_order(element):
    '''
    Organiza os candidatos por mais votados
    '''
    return int(element['seq'])

def get_cargo( cargo ):
    '''
    Obter numero do cargo
    '''
    cargos = {
        'presidente'         : '0001',
        'governador'         : '0003',
        'senador'            : '0005',
        'deputado_federal'   : '0006',
        'deputado_estadual'  : '0007',
        'deputado_distrital' : '0008',
        'prefeito'           : '0011',
        'vereador'           : '0013'
    }
    cargo = cargo.lower().replace(' ', '_')
    return cargos[ cargo ]

def get_abr( data, uf):
    '''
    Obter dados de uma UF
    '''
    for estados in data['abr']:
        if estados['cd'] == uf.upper():
            return estados

    return False

def get_nm( abr, municipio ):
    '''
    Obter dados de um município
    '''
    for municipios in abr['mu']:
        if municipios['nm'] == municipio.upper():
            return municipios

    return False

def config(api, ambiente, ciclo, pleito ):
    '''
    EA12 - Arquivo de configuração de municípios
    See https://www.tse.jus.br/eleicoes/eleicoes-2022/
        interessados-na-divulgacao-de-resultados-2022
    '''
    endpoint = api + ambiente + '/' + ciclo + '/' + pleito + '/config/mun-e00' + pleito + '-cm.json'
    with urlopen( endpoint ) as res:
        res = res.read()

    return json.loads(res)

def dados_simplificados(api, ambiente, ciclo, pleito, cargo, uf, municipio = False ):
    '''
    EA04 - Arquivo de resultado consolidado
    See https://www.tse.jus.br/eleicoes/eleicoes-2022/
        interessados-na-divulgacao-de-resultados-2022
    '''
    uf = uf.lower()

    # Obter código do cargo
    cargo = get_cargo( cargo )

    if municipio :
        endpoint = api + ambiente + '/' + ciclo + '/' + pleito + '/dados-simplificados/' + \
           uf + '/' + uf + municipio + '-c' + cargo + '-e00' + pleito + '-r.json'

    else :
        endpoint = api + ambiente + '/' + ciclo + '/' + pleito + '/dados-simplificados/' + \
           uf + '/' + uf + '-c' + cargo + '-e00' + pleito + '-r.json'

    with urlopen( endpoint ) as res:
        res = res.read()

    obj = json.loads(res)
    obj['cand'] = sorted(obj['cand'], key = get_order)
    return obj

    print( obj )
    exit()

    #if not verificar(estado + municipio, obj['dt'], obj['ht']):
        #return False

    response = config(api, ambiente, ciclo, pleito )
    b = get_abr( response, uf )
    c = get_nm( b, 'BRASÍLIA' )
    print( obj )
    print( b )
    print( c )
    exit()

    message = '#eleicao #'

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
        if i == 4:
            break

    message += '\nAtualização: ' + obj['dt']  + ' ' + obj['ht'] + \
        ', apuração: ' + obj['pst'].strip() + '%' \
        '\n#bot #eleicaobr #eleicao2020'

    return message
