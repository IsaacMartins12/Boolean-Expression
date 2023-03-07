#Arquivo de testes de software

from collections import Counter

texto = "A*B+C*A"
letras = 'ABCDE'
text_2 = []

for i in texto :
   if i in letras :
      text_2 += i
contagem_letras = Counter(text_2)

print(len((contagem_letras.keys())))