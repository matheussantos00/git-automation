import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import time

name = sys.argv[1]
description = sys.argv[2]
#  ------------------------------------------------
print('Inicializando repositório local de remoto: ' + name)
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

repositorio = {'repository[name]':name,
                 'repository[description]':description,
                 'repository[visibility]':'public',
                 'repository[auto_init]':0,
                 'repository[gitignore_template]':'',
                 'owner': usuario['login']}

a = []
#  ------------------------------------------------
site = requests.Session()
url = 'https://github.com'
url1 = url + '/new'
url2 = url + 'repositories'

login_page = site.get(url + '/login')  # request para a página de login
time.sleep(3)
if login_page.status_code == 200:
    print("Request bem sucedio na página de login")
    content = login_page.content
    soup = BeautifulSoup(content, 'html.parser')  # ler o código da página de login e formatá-lo para HTML
    usuario['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']  # token para login
    print('Token obtido e anexado ao dicionário')
    login = site.post(url + '/session', data=usuario)  # enviar login, senha e logar
    if login.status_code == 200:
        print('Login executado')
        #  ------------------------------------------------
        new_page = site.get(url + '/new')  # request para a página de criação de repositórios
        time.sleep(3)
        if new_page.status_code == 200:
            print('Acesso a página de criação de repositórios')
            content = new_page.content
            soup = BeautifulSoup(content, 'html.parser')
            for x in soup.find_all('input', attrs={'name': 'authenticity_token'}):  #  armazenar todos os tokens da página
                a.append(x.attrs['value'])

            repositorio['authenticity_token'] = a[2]  # token correto para criação de repositório

            new = site.post(url + '/repositories', data=repositorio)  # criar repositório
            if new.status_code == 200:
                print('Repositório criado')
                repo_page = site.get(url + '/matheussantos00' + '/' + repositorio['repository[name]']) # request para a página do novo repositório
                time.sleep(3)
                if repo_page.status_code == 200:
                    print('Acesso ao novo repositório')
                    content = repo_page.content
                    soup = BeautifulSoup(content, 'html.parser')
                    path = 'git remote add origin' + soup.find('button', class_="clone-url-link text-shadow-light js-git-protocol-clone-url")['data-url']  # arazenar todos os tokens da página
    else:
        site.close()  # fecha o request da página de login
site.close()  # fecha o request da página de login
