import pandas as pd
from textblob import TextBlob
from googletrans import Translator
from unidecode import unidecode
import matplotlib.pyplot as plt

'''

class Classificador():

    def __init__(self, termo):
        self.termo = termo
        self.tweets_positivos = 0
        self.tweets_negativos = 0
        self.tweets_neutros = 0
        self.total = 0

    def classifica(self, tweet):
        if self.termo in str(tweet):
            tweet_ptbr = unidecode(str(tweet))
            tweet_en = Translator().translate(tweet_ptbr)
            sentimento = TextBlob(tweet_en.text)
            if(sentimento.polarity > 0):
                self.tweets_positivos += 1
            elif(sentimento.polarity < 0):
                self.tweets_negativos += 1
            else:
                self.tweets_neutros += 1
            self.total += 1

    def sentimento(self):
        print("positivos {}".format(self.tweets_positivos))
        print("negativos {}".format(self.tweets_negativos))
        print("neutros {}".format(self.tweets_neutros))
        try:
            positivos = self.tweets_positivos / self.total
            negativos = self.tweets_negativos / self.total
            neutros = self.tweets_neutros / self.total
        except ZeroDivisionError:
            return None
        print("Classificação dos tweets: \n positivos: {0:.3g} \n negativos: {1:.3g} \n neutros: {2:.3g}".format(positivos, negativos, neutros))

        sentimento = [positivos, negativos, neutros, self.total]
        return sentimento


if __name__ == '__main__':

    tweets = pd.read_csv("limpodatacovid.csv")
    termo = "vacina"
    classificador = Classificador(termo)
    map(lambda tweet: classificador.classifica(tweet), tweets)
    # 0 - positivo, 1 - negativo, 2 - neutro, 3 - total
    sentimento = classificador.sentimento()

    grafico = plt.bar(["positivos", "negativos", "neutros"], sentimento[0:3], width=0.8)
    plt.title("Sentimento sobre o termo '{}', em proporção".format(termo))
    plt.show(grafico)

    sentimento_total = [resultado * sentimento[4] for resultado in sentimento[0:3]]
    grafico2 = plt.bar(["positivos", "negativos", "neutros"], sentimento_total, width=0.8)
    plt.title("Sentimento sobre o termo '{}', em termos absolutos".format(termo))
    plt.show(grafico2)

'''


def classifica(tweet, termo):
    tweets_positivos = 0
    tweets_negativos = 0
    tweets_neutros = 0
    total = 0
    if termo in str(tweet):
        tweet_ptbr = unidecode(str(tweet))
        tweet_en = Translator().translate(tweet_ptbr)
        sentimento = TextBlob(tweet_en.text)
        if(sentimento.polarity > 0):
            tweets_positivos += 1
        elif(sentimento.polarity < 0):
            tweets_negativos += 1
        else:
            tweets_neutros += 1
        total += 1
    print("positivos {}".format(tweets_positivos))
    print("negativos {}".format(tweets_negativos))
    print("neutros {}".format(tweets_neutros))
    try:
        positivos = tweets_positivos / total
        negativos = tweets_negativos / total
        neutros = tweets_neutros / total
    except ZeroDivisionError:
        return None
    print("Classificação dos tweets: \n positivos: {0:.3g} \n negativos: {1:.3g} \n neutros: {2:.3g}".format(positivos, negativos, neutros))

    sentimento = [positivos, negativos, neutros, total]
    return sentimento


if __name__ == '__main__':

    tweets = pd.read_csv("limpodatacovid.csv")
    termo = "vacina"
    # 0 - positivo, 1 - negativo, 2 - neutro, 3 - total
    sentimento = list(map(lambda tweet: classifica(tweet, termo), tweets))

    grafico = plt.bar(["positivos", "negativos", "neutros"], sentimento[0:3], width=0.8)
    plt.title("Sentimento sobre o termo '{}', em proporção".format(termo))
    plt.show(grafico)

    sentimento_total = [resultado * sentimento[4] for resultado in sentimento[0:3]]
    grafico2 = plt.bar(["positivos", "negativos", "neutros"], sentimento_total, width=0.8)
    plt.title("Sentimento sobre o termo '{}', em termos absolutos".format(termo))
    plt.show(grafico2)
