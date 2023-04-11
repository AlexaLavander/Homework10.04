import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_path = file_path.replace("\\","/")
        filename = file_path.split('/', )[-1]
        headers = self.get_headers()
        params = {"path": filename, "overwrite": "true"}
        href =requests.get(upload_url, headers=headers, params=params).json().get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')




if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 
    token = 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)