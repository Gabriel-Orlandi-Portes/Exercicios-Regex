import re

'''
2) Considere a seguinte string: 

O contato informado pelo cliente foi atendimento@exemplo.com. 
 
Crie um padrão regex capaz de localizar o endereço de e-mail presente na string. 

Considere que o e-mail é formado por caracteres antes do @, caracteres depois do @, um ponto e caracteres após o ponto.
'''

padrao = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+"

texto = "O contato informado pelo cliente foi atendimento@exemplo.com."

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)
