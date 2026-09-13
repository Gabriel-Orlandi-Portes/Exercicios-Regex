import re
'''
7) Considere a string abaixo: 

texto = """ 
Mariana realizou sua inscrição no evento. 
E-mail informado: mariana.silva@email.com 
 
Carlos ainda não confirmou sua participação. 
E-mail informado: carlos_22@exemplo.com.br 
 
A inscrição de Fernanda foi confirmada. 
E-mail informado: fernanda99@teste.org 
""" 
 

Crie um padrão regex capaz de localizar os endereços de e-mail presentes na string. 

Compare o resultado obtido com re.search() com o resultado obtido por re.findall(). 
'''

padrao = r"\S+@\S+\.\S+"

texto = """ 
Mariana realizou sua inscrição no evento. 
E-mail informado: mariana.silva@email.com 
 
Carlos ainda não confirmou sua participação. 
E-mail informado: carlos_22@exemplo.com.br 
 
A inscrição de Fernanda foi confirmada. 
E-mail informado: fernanda99@teste.org 
""" 

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado1)
print(encontrado2)