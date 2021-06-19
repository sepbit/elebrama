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

import unittest
from os import environ
from sepbit.cabrama.mastodon import statuses, delete


class MastodonTest(unittest.TestCase):
    '''
    Test mastodon.py module
    '''

    def test_statuses(self):
        '''
        Test statuses function
        '''
        result = statuses(
            environ['INSTANCE'],
            environ['TOKEN'],
            data={
                'status': 'teste',
                'language': 'por',
                'visibility': 'public'
            }
        )

        self.assertTrue(result)

        '''
        Test delete function
        '''
        self.assertTrue(
            delete(
                environ['INSTANCE'],
                environ['TOKEN'],
                result['id']
            )
        )


if __name__ == '__main__':
    unittest.main()
