import re

'''
9) Considere os dados fictícios: 

texto = """ 
Biblioteca Machado de Assis 
Telefone: (21) 3456-7821 
Cidade: Rio de Janeiro - RJ 
 
Biblioteca Carolina Maria de Jesus 
Telefone: (11) 2987-4512 
Cidade: São Paulo - SP 
 
Biblioteca Cora Coralina 
Telefone: (62) 3678-9012 
Cidade: Goiânia - GO 
 
Biblioteca Graciliano Ramos 
Telefone: (82) 3123-7788 
Cidade: Maceió - AL""" 
 

Crie um padrão regex capaz de localizar todos os telefones no formato (XX) XXXX-XXXX. 

O padrão deverá considerar os parênteses, o espaço e o hífen existentes nos números. 
'''

padrao = r'\([0-9]{2}\) [0-9]{4}-[0-9]{4}'

texto = """ 
Biblioteca Machado de Assis 
Telefone: (21) 3456-7821 
Cidade: Rio de Janeiro - RJ 
 
Biblioteca Carolina Maria de Jesus 
Telefone: (11) 2987-4512 
Cidade: São Paulo - SP 
 
Biblioteca Cora Coralina 
Telefone: (62) 3678-9012 
Cidade: Goiânia - GO 
 
Biblioteca Graciliano Ramos 
Telefone: (82) 3123-7788 
Cidade: Maceió - AL""" 

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)