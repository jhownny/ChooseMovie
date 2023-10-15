import requests
from keypath import chave_API



url = f'https://api.themoviedb.org/3/discover/movie?language=pt-BR&with_release_type=5&api_key={chave_API}'
r = requests.get(url)
data = r.json()

print(data)