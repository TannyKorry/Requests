import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = self.url + 'upload'
        headers = self._get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def _add_folder(self, path):
        headers = self._get_headers()
        requests.put(f'{self.url}?path={path}', headers=headers)

    def _upload(self, file_path, path_to_file):
        link_dict = self._get_upload_link(file_path=file_path)
        href = link_dict['href']
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def upload_files_from_a_list(self, path_to_file_list):
        for path_to_file in path_to_file_list:
            directory, file_name = path_to_file.split('/')
            uploader._add_folder(directory)
            uploader._upload(path_to_file, path_to_file)


if __name__ == '__main__':

    with open('ТокенYa.txt', 'r') as f:
        token = f.read().strip()
    uploader = YaUploader(token)

    path_to_file_list = ['Requests/text.txt', 'Портфолио/photo.jpg', 'ООП дз/OOP.py']

    uploader.upload_files_from_a_list(path_to_file_list)