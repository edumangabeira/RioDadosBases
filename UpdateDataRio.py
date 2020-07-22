# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 00:47:00 2020

@author: gui_s
"""


#import csv
#import gzip
import io
import gspread
import pandas as pd
from urllib.request import Request, urlopen
from oauth2client.service_account import ServiceAccountCredentials

########################################
######### Importação dos dados #########
########################################

## Função para download dos dados do brasil.io (https://gist.github.com/turicas/3e3621d61415e3453cd03a1997f7473f)
#def download_brasilio_table(dataset, table_name):


#### PRIMEIRO LINK (dados individuais com CEP) ####
url = "http://pcrj.maps.arcgis.com/sharing/rest/content/items/b54234c151aa4d01b488dc12aafd5574/data"
request = Request(url, headers={"User-Agent": "python-urllib"})
response = urlopen(request)
data = response.read()
s = data.decode("ISO-8859-1")

dados_cep = pd.read_csv(io.StringIO(s), sep = ";")
#dados_cep.to_excel("teste1.xlsx")
dados_cep["dt_óbito"] = dados_cep["dt_óbito"].fillna("NA")
dados_cep = dados_cep.fillna("NA")


#### SEGUNDA URL #######
url = "http://pcrj.maps.arcgis.com/sharing/rest/content/items/754cc0698129404ba8bfb053cbdbd158/data"
request = Request(url, headers={"User-Agent": "python-urllib"})
response = urlopen(request)
data = response.read()
s = data.decode("ISO-8859-1")

dados_sociodem = pd.read_csv(io.StringIO(s), sep = ";")
#dados_sociodem["dt_óbito"][dados_sociodem["dt_óbito"].isnull()] = "NA"
dados_sociodem["dt_óbito"] = dados_sociodem["dt_óbito"].fillna("NA")
dados_sociodem = dados_sociodem.fillna("NA")

#dados_sociodem.to_excel("teste2_sociodem.xlsx")

#### Upload para o sheets ####
# Autenticação
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # Queremos acessar o spreadsheets para atualizar os arquivos
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds) 

## dados cep
munic_cep = client.open("dados_munic_CEP").sheet1
munic_cep.update([dados_cep.columns.values.tolist()] + dados_cep.values.tolist())

## dados sociodem
munic_sociodem = client.open("dados_munic_sociodemograficos").sheet1
munic_sociodem.update([dados_sociodem.columns.values.tolist()] + dados_sociodem.values.tolist())




