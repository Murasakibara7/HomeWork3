import requests
from pprint import pprint

lst = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'
respon = requests.get(url)
respon_2 = respon.json()
print()
for i in lst:
    for j in respon_2:
        if i == j['name']:
            print(f"Имя: {i}, интелект: {j['powerstats']['intelligence']}")


token =
def headler():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


url = 'https://cloud-api.yandex.net:443/'
param = 'v1/disk'


# 'v1/disk/resources' #'v1/disk/public/resources' #'v1/disk/trash/resources'
def files():
    url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = headler()
    response = requests.get(url=url, headers=headers)
    return response.json()


def upload_file(file, path=''):
    name = file.split('/')[-1]
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = headler()
    if path != '':
        params = {'path': path + '/' + name, 'overwrite': 'true'}
    else:
        params = {'path': name, 'overwrite': 'true'}
    response = requests.get(url, headers=headers, params=params)
    resp = response.json()
    result = resp.get('href')
    response = requests.put(result, data=open(file, 'rb'))
    response.raise_for_status()
    if response.status_code == 201:
        print('Готово')


if __name__ == '__main__':
    pprint(files())
    upload_file('ttetr.txt')