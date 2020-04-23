import pandas as pd
import requests
from bs4 import BeautifulSoup

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

site = requests.Session()
url_login = 'https://github.com/login'
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
    else:
        site.close()  # fecha o request da página de login
