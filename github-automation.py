import requests
from bs4 import BeautifulSoup
import sys
import time


class GitHub:
    def __init__(self):
        self.name = sys.argv[1]
        self.description = sys.argv[2]
        self.tokens = []
        self.url = 'https://github.com'
        print('Inicializando repositório local e remoto: ' + self.name)

    def login_file(self):
        try:
            file = open('login.txt', 'x')
            file.write(input('login: ') + '\n')
            file.write(input('senha: '))
            file.close()
        except:
            pass
        finally:
            file = open('login.txt', 'r')
            self.usuario = {'login': file.readline().replace('\n', ''),
                            'password': file.readline()}
            file.close()

    def repository(self):
        self.repo = {'repository[name]': self.name,
                     'repository[description]': self.description,
                     'repository[visibility]': 'public',
                     'repository[auto_init]': 0,
                     'repository[gitignore_template]': '',
                     'owner': self.usuario['login']}

    def scrape(self):
        site = requests.Session()
        login_page = site.get(self.url + '/login')  # request para a página de login
        time.sleep(3)

        if login_page.status_code == 200:
            print("Acesso à página de login")
            content = login_page.content
            soup = BeautifulSoup(content, 'html.parser')  # ler o código da página de login e formatá-lo para HTML
            self.usuario['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']  # token para login
            login = site.post(self.url + '/session', data=self.usuario)  # enviar login, senha e logar

            if login.status_code == 200:
                print('Login executado')
                new_page = site.get(self.url + '/new')  # request para a página de criação de repositórios
                time.sleep(3)

                if new_page.status_code == 200:
                    print('Acesso à página de criação de repositórios')
                    content = new_page.content
                    soup = BeautifulSoup(content, 'html.parser')

                    for x in soup.find_all('input', attrs={'name': 'authenticity_token'}):
                        self.tokens.append(x.attrs['value'])  # armazenar todos os tokens da página

                    self.repo['authenticity_token'] = self.tokens[2]  # token correto para criação de repositório
                    new = site.post(self.url + '/repositories', data=self.repo)  # criar repositório

                    if new.status_code == 200:
                        print('Repositório criado')

            else:
                site.close()  # fecha o request em caso de erro
        site.close()          # fecha o request ao fim do acesso


if __name__ != 'main':
    app = GitHub()
    app.login_file()
    app.repository()
    app.scrape()
