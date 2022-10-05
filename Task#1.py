import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
hero_list = ['Hulk', 'Captain America', 'Thanos']
iq = {}
for el in response.json():
    name_hero = el['name']
    if name_hero in hero_list:
        iq[name_hero] = el['powerstats']['intelligence']

for k, v in iq.items():
    if v == max(iq.values()):
        print(f'Из списка супергероев {hero_list} самый умный {k},'
              f' так как его интелект равен {v}')
