import socket

"""
Em redes de computadores, reverse DNS lookup (ou reverse DNS resolution, rDNS)
é a determinação de um nome de domínio associado a um endereço IP na Internet.
"""

try:
    ip = socket.gethostbyname('www.google.com.br')
except socket.gaierror:
    print('Domínio não esta disponível')
else:
    print('O domínio está disponível')
