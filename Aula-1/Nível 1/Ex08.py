import re

'''
8) Considere os registros fictícios abaixo, criados para uma atividade sobre escritores brasileiros: 

texto = """ 
Machado de Assis (1839-1908) - escritor brasileiro. 
Contato: machado.assis@literatura.com 
Cidade: Rio de Janeiro - RJ 
 
Carolina Maria de Jesus (1914-1977) - escritora brasileira. 
Contato: carolina.jesus@literatura.com 
Cidade: Sacramento - MG 
 
Conceição Evaristo (1946) - escritora brasileira. 
Contato: conceicao.evaristo@literatura.com 
Cidade: Belo Horizonte - MG 
 
Carlos Drummond de Andrade (1902-1987) - poeta brasileiro. 
Contato: carlos.drummond@literatura.com 
Cidade: Itabira - MG 
""" 
 

Os e-mails são fictícios e utilizados apenas para o exercício. 

Crie um padrão regex capaz de localizar todos os anos formados por quatro algarismos presentes na string. 

Observe que alguns escritores possuem dois anos no registro, enquanto outros possuem apenas um. 
'''

padrao = r"[0-9]{4}"

texto = """ 
Machado de Assis (1839-1908) - escritor brasileiro. 
Contato: machado.assis@literatura.com 
Cidade: Rio de Janeiro - RJ 
 
Carolina Maria de Jesus (1914-1977) - escritora brasileira. 
Contato: carolina.jesus@literatura.com 
Cidade: Sacramento - MG 
 
Conceição Evaristo (1946) - escritora brasileira. 
Contato: conceicao.evaristo@literatura.com 
Cidade: Belo Horizonte - MG 
 
Carlos Drummond de Andrade (1902-1987) - poeta brasileiro. 
Contato: carlos.drummond@literatura.com 
Cidade: Itabira - MG 
""" 

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)