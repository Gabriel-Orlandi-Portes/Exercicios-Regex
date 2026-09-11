import re
'''
6) (DEBUG) O programa abaixo deveria procurar um e-mail dentro da string. Entretanto, os argumentos de re.search() e re.findall() foram colocados na ordem errada. 

Identifique e corrija o problema.  
 
padrao = r"\S+@\S+\.\S+" 
 
texto = "O e-mail informado foi aluno@exemplo.com" 
 
encontrado1 = re.search(texto, padrao) 
encontrado2 = re.findall(texto, padrao) 
 
print(encontrado1) 
print(encontrado2) 
'''

padrao = r"\S+@\S+\.\S+" 
 
texto = "O e-mail informado foi aluno@exemplo.com" 
 
encontrado1 = re.search(padrao, texto) 
encontrado2 = re.findall(padrao, texto) 
 
print(encontrado1) 
print(encontrado2) 