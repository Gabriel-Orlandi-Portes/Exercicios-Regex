import re

'''
5) (DEBUG) O programa abaixo deveria encontrar números de pedido formados por exatamente quatro algarismos. Porém, o regex utilizado está encontrando também números com outras quantidades de algarismos. 

Analise o código, identifique o problema e faça a correção necessária. 

 
padrao = r"[0-9]+" 
 
texto = "Os pedidos 5832 e 7419 foram enviados para o setor 47." 
 
encontrado1 = re.search(padrao, texto) 
encontrado2 = re.findall(padrao, texto) 
 
print(encontrado1) 
print(encontrado2) 
 

O resultado de encontrado2 deve conter os números 5832 e 7419, mas não o número 47. 
'''

padrao = r"[0-9]{4}" 
 
texto = "Os pedidos 5832 e 7419 foram enviados para o setor 47." 
 
encontrado1 = re.search(padrao, texto) 
encontrado2 = re.findall(padrao, texto) 
 
print(encontrado1) 
print(encontrado2) 