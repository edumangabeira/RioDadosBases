import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)


with open("busca_por_palavras.csv","r", encoding='utf-8') as resultado:
	palavras= pd.read_csv(resultado)
	palavras_covid = client.open_by_key("1gEu954wNAQSVgjWROktRjtDDqDJZ__VSdzRBcebb0hw").sheet1
	palavras_covid.update([palavras.columns.values.tolist()] + palavras.values.tolist())