import requests

res = requests.get('https://pokeapi.co/api/v2/ability/2')
print(res.text)
