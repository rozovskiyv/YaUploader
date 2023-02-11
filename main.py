import requests
import os


class YDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_file_list(self):
        res_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(res_url, headers=headers)
        return response.json()

    def get_upload_link(self, file_path):
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)
        return response.json()

    def upload(self, path, name):
        link = self.get_upload_link(name)
        href = link.get('href')
        response = requests.put(href, data=open(os.path.join(path, name), 'rb'))
        res_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


if __name__ == '__main__':
    path_to_file = 'C:\\Python'
    file_name = '5.txt'
    ya = YDisk('y0_AgAAAAAwperBAADLWwAAAADbzbGAuN0eAfDJQoei71SVGGczDxEntuQ')
    ya.upload(path_to_file, file_name)