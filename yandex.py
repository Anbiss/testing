import requests
import unittest

TOKEN = 'y0_AgAAAAAhSJvjAADLWwAAAADWF-wFrH73fkDXTEqf_8B0MK_4ShIotZQ'

URL = 'https://cloud-api.yandex.net/v1/disk/resources'

HEADERS = {'Authorization': f'OAuth {TOKEN}'}

FOLDER = 'тест'


def folder_creation(url=URL, headers=HEADERS):
    response = requests.put(f'{url}?path={FOLDER}', headers=headers)
    return response.status_code


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_folder_creation(self):
        self.assertEqual(folder_creation(), 201)

    def test_invalid_url(self):
        with self.assertRaises(requests.exceptions.RequestException):
            folder_creation(url="invalid_url")

    def test_invalid_token(self):
        invalid_headers = {'Authorization': 'invalid_token'}
        self.assertNotEqual(folder_creation(headers=invalid_headers), 201)

if __name__ == '__main__':
    unittest.main()
