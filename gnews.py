import os
import requests
import json
import time

api_key = os.environ['GNEWS']
payload = {'country': 'br', 'lang': 'pt-BR'}

url = "https://gnews.io/api/v3/topics/health?&token={}".format(api_key)

with open("noticias.json", 'a') as noticias:
	artigo = requests.get(url, params=payload)
	json.dump(artigo.json(), noticias)