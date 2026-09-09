import re

'''
4) Considere a seguinte string: 

O produto selecionado possui o código ABC-4821 e está disponível. 
 

Crie um padrão regex capaz de localizar o código do produto. 

O código possui três letras maiúsculas, um hífen e quatro algarismos. 

Procure construir o padrão utilizando os intervalos [A-Z] e [0-9]. 
'''

padrao = r'[A-Z]{3}-[0-9]{4}'

texto = "O produto selecionado possui o código ABC-4821 e está disponível."

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)