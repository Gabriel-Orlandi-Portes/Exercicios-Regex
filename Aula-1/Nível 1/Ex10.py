import re

'''
10) (DEBUG) O programa deveria encontrar todos os telefones no formato (XX) XXXX-XXXX. Entretanto, o regex procura uma quantidade incorreta de algarismos em uma das partes do telefone. 

Encontre o problema e faça a correção. 
 
padrao = r"\([0-9]{2}\) [0-9]{5}-[0-9]{4}" 
 
texto = """ 
Biblioteca Central 
Telefone: (11) 3456-7821 
 
Biblioteca Municipal 
Telefone: (21) 2876-4512 
 
Biblioteca Universitária 
Telefone: (31) 3678-9012 
""" 
 
encontrado1 = re.search(padrao, texto) 
encontrado2 = re.findall(padrao, texto) 
 
print(encontrado1) 
print(encontrado2) 
'''

padrao = r"\([0-9]{2}\) [0-9]{4}-[0-9]{4}" 
 
texto = """ 
Biblioteca Central 
Telefone: (11) 3456-7821 
 
Biblioteca Municipal 
Telefone: (21) 2876-4512 
 
Biblioteca Universitária 
Telefone: (31) 3678-9012 
""" 
 
encontrado1 = re.search(padrao, texto) 
encontrado2 = re.findall(padrao, texto) 
 
print(encontrado1) 
print(encontrado2) 