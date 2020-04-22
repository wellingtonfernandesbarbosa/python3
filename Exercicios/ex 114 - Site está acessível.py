import urllib.request  # Caso essa bilblioteca deixe de funcionar, pode ser devido a mudanças
# porque a mesma não é padrão do Python

try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site Google não está acessivel no momento.')
else:
    print('Consegui acessar o site Google com sucesso!')
