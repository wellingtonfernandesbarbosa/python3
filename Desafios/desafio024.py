city = str(input('Digite o nome de sua cidade: ')).strip()
print('Sua cidade tem a palavra Santo no nome: {}'.format(city[:5].capitalize() == 'Santo'))
