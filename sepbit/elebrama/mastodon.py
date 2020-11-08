'''
Mastodon.py Simple statuses Mastodon
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
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def statuses(instance, token, data):
    '''
    Mastodon statuses post
    See https://docs.joinmastodon.org/methods/statuses
    '''

    data = urlencode(data)
    data = data.encode('ascii') # data should be bytes

    req = Request(
        'https://' + instance + '/api/v1/statuses',
        data,
        headers={
            'Content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + token
        },
        method='POST'
    )
    with urlopen(req) as res:
        res = res.read()

    return json.loads(res)


def delete(instance, token, s_id):
    '''
    Mastodon statuses delete
    See https://docs.joinmastodon.org/methods/statuses
    '''
    req = Request(
        'https://' + instance + '/api/v1/statuses/' + s_id,
        headers={
            'Authorization': 'Bearer ' + token
        },
        method='DELETE'
    )
    with urlopen(req) as res:
        res = res.read()

    return json.loads(res)
