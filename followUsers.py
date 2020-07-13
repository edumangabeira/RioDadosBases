import tweepy
import time


'''
Segue os usuários do twitter da nossa lista de fontes.

Checar todos as fontes que um usuário segue pode levar algum tempo.

'''

def fontes(arquivo):

    with open(arquivo,"r",encoding = "UTF-8") as arq_fontes:
        fontes = arq_fontes.readlines()
        fontes = [fonte.replace("\n","") for fonte in fontes]
        fontes = [fonte.replace("\u200f","") for fonte in fontes]

    return fontes

def check(user):
    friends = api.friends_ids(user)
    friends = [api.get_user(friend).screen_name for friend in friends]
    return friends


if __name__ == '__main__':
    

    arquivo = "fontes.txt"
    fontes = fontes(arquivo)

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = "palestrinha157"

    check = input("deseja checar as contas que o usuário segue? s - sim n - não")

    if check != 'n':
        friends = check(user)
    else:
        friends = []

    for fonte in fontes:
        if fonte not in friends:
            api.create_friendship(fonte)
            print("{} followed".format(fonte))