import pandas as pd
import requests
from bs4 import BeautifulSoup

#  ------------------------------------------------
try:
    file = open('login.txt', 'x')
    file.write(input('login: ')+'\n')
    file.write(input('senha: '))
    file.close()
except:
    pass
finally:
    file = open('login.txt', 'r')
    usuario = {'login': file.readline().replace('\n', ''),
               'password': file.readline()
               }
    file.close()
#  ------------------------------------------------

repositorio = {'repository[name]':'testando',
                 'repository[description]':'testando',
                 'repository[visibility]':'public',
                 'repository[auto_init]':0,
                 'repository[gitignore_template]':'',
                 'owner':'matheussantos00'}

a = []
#  ------------------------------------------------
site = requests.Session()
url_login = 'https://github.com/login'
url_new = 'https://github.com/new'

git_login = site.get(url_login)  # request para a página de login
if git_login.status_code == 200:
    print("Request bem sucedio na página de login")
    content = git_login.content
    soup = BeautifulSoup(content, 'html.parser')  # ler o código da página de login e formatá-lo para HTML
    usuario['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']  # token para login
    print('Token obtido e anexado ao dicionário')
    login = site.post('https://github.com/session', data=usuario)  # enviar login, senha e logar
    if login.status_code == 200:
        print('Login executado')
        #  ------------------------------------------------
        git_new = site.get(url_new)  # request para a página de criação de repositórios
        if git_new.status_code == 200:
            print('Acesso a página de criação de repositórios')
            content = git_new.content
            soup = BeautifulSoup(content, 'html.parser')

            for x in soup.find_all('input', attrs={'name': 'authenticity_token'}):  #  armazenar todos os tokens da página
                a.append(x.attrs['value'])

            repositorio['authenticity_token'] = a[2]  # token correto para criação de repositório

            new = site.post('https://github.com/repositories', data=repositorio)  # criar repositório
            if new.status_code == 200:
                print('Repositório criado')

    else:
        site.close()  # fecha o request da página de login
site.close()  # fecha o request da página de login