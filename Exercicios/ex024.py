city = str(input('{}Digite o nome de sua cidade: '.format('\033[33m'))).strip()
print('{}O nome da sua cidade começa com Santo: {}'.format('\033[36m', city[:5].capitalize() == 'Santo'))
