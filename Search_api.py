import pymongo
import time
import tweepy
import datetime


# conecta ao banco mongo
mongo = pymongo.MongoClient()
db = mongo['RioEmDados']
collection = db['covid']

# autentica chaves
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# seleciona termos a serem coletados por dia da semana
hoje = datetime.datetime.today().weekday()
semana = {'seg':['vacina','máscara','leitos'], 
          'ter': ['covid','gripezinha','UTI'], 
          'qua': ['quarentena','pandemia','isolamento'], 
          'qui': ['hospital','recuperados','coronavirus'], 
          'sex': ['SARS-CoV-2','vírus','covid-19'], 
          'sab': ['infectologista','covid19','OMS'], 
          'dom': ['respiradores','medicamento','infectados']}

for codigo, dia in enumerate(semana.keys()):
	if codigo == hoje:
		termos = semana[dia]

# executa coleta
for termo in termos:
	dados = api.search(q=termo)
	print(dados)
	collection.insert_one(dados)
	print("Termo {} inserido na coleção {} do banco {}".format(termo, collection, db))
	if termo.index() != len(termos):
		time.sleep(15*60)
	else:
		print("Coleta finalizada")