# Consumo de API com Python

import requests
from datetime import datetime

r = requests.get('https://api.github.com/users/kauandragues')
inf_usuario_git = r.json()
print(f"login: {inf_usuario_git['login']}")
print(f"Nome: {inf_usuario_git['name']}")
print(f"Quantidade de Repositórios: {inf_usuario_git['public_repos']
                                     + inf_usuario_git['public_gists']}")
