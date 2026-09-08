import re
'''
3) Considere a seguinte string: 

A atividade foi marcada para 18/09/2026, às 19 horas. 
 
Crie um padrão regex capaz de localizar uma data no formato DD/MM/AAAA. 

Utilize intervalos como [0-9] e a quantidade de ocorrências necessária para representar dia, mês e ano.
'''

padrao = r"[0-9]{2}/[0-9]{2}/[0-9]{4}"

texto = "A atividade foi marcada para 18/09/2026, às 19 horas."

encontrado1 = re.search(padrao, texto)
encontrado2 = re.findall(padrao, texto)

print(encontrado2)