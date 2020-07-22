# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:47:56 2020

@author: Guilherme Santos
"""

import csv
import gzip
import io
import gspread
import pandas as pd
from urllib.request import Request, urlopen
from oauth2client.service_account import ServiceAccountCredentials

########################################
######### Importação dos dados #########
########################################

## Função para download dos dados do brasil.io (https://gist.github.com/turicas/3e3621d61415e3453cd03a1997f7473f)
def download_brasilio_table(dataset, table_name):
    url = f"https://data.brasil.io/dataset/{dataset}/{table_name}.csv.gz"
    request = Request(url, headers={"User-Agent": "python-urllib"})
    response = urlopen(request)
    return gzip.decompress(response.read()).decode("utf-8")


# Passe o nome da tabela para a função, como "caso", "caso_full", "obito_cartorio":
data = download_brasilio_table("covid19", "caso_full")
reader = csv.DictReader(io.StringIO(data))

dados = pd.DataFrame(reader)

dados = dados[dados.state == "RJ"] #todos os dados pro estado

dados_estado = dados[dados.place_type == "state"] #dados agregados para o estado
dados_estado = dados_estado.drop("city", axis = 1)

dados_municipios = dados[dados.place_type == "city"] # dados apenas de municípios
dados_munic_rj = dados[dados.city == "Rio de Janeiro"] # dados dos municípios do RJ


######### Upload sheets #########

# Autenticação
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # Queremos acessar o spreadsheets para atualizar os arquivos
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Guilherme Santos\\Downloads\\redcov19\\client_secret.json', scope)
client = gspread.authorize(creds) 


## Upload dos dados do município do rj
municipio = client.open("municipio_rj").sheet1
municipio.update([dados_munic_rj.columns.values.tolist()] + dados_munic_rj.values.tolist())

## Upload dos dados estado
estado = client.open("estado_rj_agregado").sheet1
estado.update([dados_estado.columns.values.tolist()] + dados_estado.values.tolist())

## todos os municipios
munic_desag = client.open("desagregado_munic").sheet1
munic_desag.update([dados_municipios.columns.values.tolist()] + dados_municipios.values.tolist())








