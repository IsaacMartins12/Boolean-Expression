sinais = {'{','}','[',']','(',')'}

def deletar (aux,pos,exp3,indice,valor) :  ## Deleta os elementos que foram operados

          del(aux[pos-1:pos+2])
          del(exp3[pos-1+indice:indice+pos+2])
          aux.insert(pos-1, valor)
          exp3.insert(pos-1+indice, valor)
          '''for i in range (0,len(exp3)) :
               print(exp3[i] , end = ' ') 
          print('\n')'''

def somar (exp3,indice,aux,op) :  ## Realiza a operação de soma

          if op == 1 :
            pos = aux.index('+')
            valor = (int(aux[pos-1]) + int(aux[pos+1]))
            if valor >= 1 : valor = 1
            deletar(aux,pos,exp3,indice,valor)
            return valor
          else :
             pos = exp3.index('+')
             valor = (int(exp3[pos-1]) +int(exp3[pos+1]))
             if valor >= 1 : valor = 1
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             '''for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')'''
             return valor

"""def subtrair (exp3,indice,aux,op) :  ## Realiza a operação de subtração

          if op == 1 :
            pos = aux.index('-')
            valor = (int(aux[pos-1]) -int(aux[pos+1]))
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('-')
             valor = (int(exp3[pos-1]) -int(exp3[pos+1]))
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             '''for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')'''
             return valor
"""

def multiplicar (exp3,indice,aux,op) :   ## Realiza a operação de multiplicação
 
          if op == 1 :
            pos = aux.index('*')
            valor = (int(aux[pos-1]) *int(aux[pos+1]))
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else :
             pos = exp3.index('*')
             valor = (int(exp3[pos-1]) *int(exp3[pos+1]))
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             '''for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')'''
             return valor
"""""
def dividir (exp3,indice,aux,op) :  ## Realiza a operação de divisão

          if op == 1 :
            pos = aux.index('/')
            valor = (int(aux[pos-1]) /int(aux[pos+1]))
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('/')
             valor = (int(exp3[pos-1]) /int(exp3[pos+1]))
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             '''for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')'''
             return valor
"""""
"""""
def potencia (exp3,indice,aux,op) :   ## Realiza a operação de potência

          if op == 1 :
            pos = aux.index('^')
            valor = (int(aux[pos-1]) **int(aux[pos+1]))
            deletar(aux,pos,exp3,indice,valor) 
            return valor
          else : 
             pos = exp3.index('^')
             valor = (int(exp3[pos-1]) **int(exp3[pos+1]))
             del(exp3[pos-1:pos+2])
             exp3.insert(pos-1, valor)
             '''for i in range (0,len(exp3)) :
                print(exp3[i] , end = ' ')
             print('\n')'''
             return valor
"""