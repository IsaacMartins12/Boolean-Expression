import calculos.operacoes_exp as operacoes_exp
import calculos.validacao_exp as validacao_exp
from prettytable import PrettyTable


def gera_tabela(numero,expression_1,expression) :   # Functionn responsable by show true-tables
   
   if numero == "2" :

      table = PrettyTable(["A", "B", "S"])

      table.add_row(["0","0",(calcula(expression_1))])
      expressao_mudada = muda_valor(expression,0,1)
      table.add_row(["0","1",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,0)
      table.add_row(["1","0",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,1)
      table.add_row(["1","1",(calcula(expressao_mudada))])
      
      return (table)

   if numero == "3" :
    
      table = PrettyTable(["A", "B", "C", "S"])

      table.add_row(["0","0","0",(calcula(expression_1))])
      expressao_mudada = muda_valor(expression,0,0,1)
      table.add_row(["0","0","1",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,0,1,0)
      table.add_row(["0","1","0",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,0,1,1)
      table.add_row(["0","1","1",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,0,0)
      table.add_row(["1","0","0",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,0,1)
      table.add_row(["1","0","1",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,1,0)
      table.add_row(["1","1","0",(calcula(expressao_mudada))])
      expressao_mudada = muda_valor(expression,1,1,1)
      table.add_row(["1","1","1",(calcula(expressao_mudada))])
      
      return (table)

def muda_valor(expression,value_a,value_b,value_c=0) :

  expression_1 = []
  for i in expression :
    if i == "A" : expression_1.append(value_a)
    elif i == "B" : expression_1.append(value_b)
    elif i == "C" : expression_1.append(value_c)
    else : expression_1.append(i)
  return expression_1

def importa_expressao_booleana() :
   
  expression = input("Sua expressao --> ")
  variaveis = input("Numero de variaveis --> ")
  value_c = "0"
  value_b = "0"
  value_a = "0"
  expression_1 = []

  for i in expression :
    if i == "A" : expression_1.append(value_a)
    elif i == "B" : expression_1.append(value_b)
    elif i == "C" : expression_1.append(value_c)
    else : expression_1.append(i)

  gera_tabela(variaveis,expression_1,expression)

  return expression_1


def apresenta_menu() :

    exp = []
    exp = importa_expressao_booleana()
    print("\n")
    return exp

def conta_especial(exp1,indice) :        ## Realiza conta que tenham elementos especiais
 
   op = 1

   if '(' in exp1 and ')' in exp1 : aux = exp1[exp1.index('(')+1:exp1.index(')')]
   elif '[' in exp1 and ']' in exp1 : aux = exp1[exp1.index('[')+1:exp1.index(']')]
   elif '{' in exp1 and '}' in exp1 : aux = exp1[exp1.index('{')+1:exp1.index('}')]

   while(True) :

     if '*' in aux and '/' in aux :

      if aux.index("*") < aux.index("/") :
          if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op) 
          if '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)
          if '/' in aux : valor = operacoes_exp.dividir(exp1,indice,aux,op)

      else : 

        if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op) 
        if '/' in aux :valor  =  operacoes_exp.dividir(exp1,indice,aux,op)
        elif '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)

     else :

      if '^' in aux : valor = operacoes_exp.potencia(exp1,indice,aux,op)
      elif '/' in aux : valor = operacoes_exp.dividir(exp1,indice,aux,op)
      elif '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)
      elif '-' in aux :  valor = operacoes_exp.subtrair(exp1,indice,aux,op)
      elif '+' in aux : valor = operacoes_exp.somar(exp1,indice,aux,op)
      
      if len(aux) == 1 : return(aux[0]) 

def calcula(exp) :  ## Realiza conta que nao tenham elementos especiais

 expressao = exp
 valor = paren = 0 
 while (True) :

  if '(' in expressao and ')' in expressao :

   paren = expressao.index('(')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(')')+1])
   expressao.insert(paren,resposta)

  else : break

 while (True) :
  if '[' in expressao and ']' in expressao :

   paren = expressao.index('[')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index(']')+1])
   expressao.insert(paren,resposta)

  else : break 

 while (True) :

  if '{' in expressao and '}' in expressao :
   paren = expressao.index('{')
   resposta = conta_especial(expressao,paren+1)
   del(expressao[paren:expressao.index('}')+1])
   expressao.insert(paren,resposta)
  else : break 
 
 op = 0


 while(True) :           ## Realiza a sequencia de operacoes
  try :  
   if '*' in expressao and '/' in expressao :

    if expressao.index("*") < expressao.index("/") :

        if '^' in expressao :  valor = operacoes_exp.potencia(expressao,1,1,op)
        if '*' in expressao :  valor = operacoes_exp.multiplicar(expressao,1,1,op)
        if '/' in expressao :  valor = operacoes_exp.dividir(expressao,1,1,op)

    else : 

      if '^' in expressao :  valor = operacoes_exp.potencia(expressao,1,1,op)
      if '/' in expressao :  valor = operacoes_exp.dividir(expressao,1,1,op)
      elif '*' in expressao :  valor =  operacoes_exp.multiplicar(expressao,1,1,op)

   else : 

    if '^' in expressao : valor = operacoes_exp.potencia(expressao,1,1,op)
    elif '/' in expressao : valor =  operacoes_exp.dividir(expressao,1,1,op)
    elif '*' in expressao : valor = operacoes_exp.multiplicar(expressao,1,1,op)
    elif '-' in expressao : valor =  operacoes_exp.subtrair(expressao,1,1,op)
    elif '+' in expressao : valor = operacoes_exp.somar (expressao,1,1,op)
    elif len(expressao) == 1 : return(expressao[0]) 

  except :
    return 1


print ('\n\n'+'='*30 + ' CALCULADORA DE EXPRESSOES NUMÉRICAS BOOLEANAS ' + '='*30) 
print ('\n (*) - PORTA AND --> exemplo : A*B ')
print ('\n (+) - PORTA OR --> exemplo : A + B ')
print ('\n (") - PORTA NOT --> exemplo : A"+B"')

print("\n\n Exemplo de expressao válida : A*B+A+B*A \n\n")

while (True) :
 exp = apresenta_menu()
 if (validacao_exp.valida_expressao(exp) and calcula(exp)!=1):
    #print(f'\n\nO valor da sua expressao é {calcula(exp)} \n')
    novamente = input(('\n\nQuer colocar outra expressao ? [S/N] : '))
    if novamente.upper() == 'N' :
      break
    
  
