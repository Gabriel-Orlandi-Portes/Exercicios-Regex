import re

'''
1) Considere a seguinte string: 

O pedido 5832 foi enviado para o setor 47. 
 
Crie um padrão regex capaz de localizar sequências formadas por exatamente quatro algarismos. 

Utilize re.search() para localizar a primeira ocorrência e re.findall() para localizar todas as ocorrências. 
'''

padrao = r"[0-9]{4}"

texto = "5832"

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)