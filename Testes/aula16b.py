pessoa = ('Wellington', 27, 'masculino', 75.6, 1.73)  # Uma tupla pode receber diferentes tipos de valores
print(f'{pessoa[0]} tem {pessoa[1]} anos, é do sexo {pessoa[2]}, pesa {pessoa[3]} kilos e tem {pessoa[4]} de altura')
del pessoa  # A tupla não pode ser alterada, mas pode ser apagada
pessoa = ('presidente', 'idiota', 4)  # E ser novamente definida
print(f'Nosso {pessoa[0]} é um {pessoa[1]} e essa porra vai durar {pessoa[2]} anos.'
      f'\nMas acho que ele cai primeiro! :-)')
