import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = self.url + 'upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def add_folder(self, path):
        '''Функция создает папку на Яндекс.Диск'''
        headers = self.get_headers()
        requests.put(f'{self.url}?path={path}', headers=headers)

    def upload(self, file_path, filename):
        link_dict = self._get_upload_link(file_path=file_path)
        href = link_dict['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_file = ['Requests/Avatar.jpg']
    token = 'y0_AgAAAAACJgUTAADLWwAAAADQUu4Ssvs6XLpRRLSvjZbPuH2KGFqk8UA'
    uploader = YaUploader(token)
    directory_list = ['Requests', 'Портфолио', 'ООП дз']
    folder = uploader.add_folder(directory_list)
    # result = uploader.upload(path_to_file)
    # result = uploader.upload(uploader.add_folder('net_logy')+'/Avotor.jpg', 'Requests/Avatar.jpg')
    # pprint(folder)