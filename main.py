from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
  return ("<h3>Insira uma expressao booleana na barra de navegacao<h3>")

@app.route('/<expressao_url>')
def tabela(expressao_url):
    
    import calculos.operacoes_exp as operacoes_exp
   
    def gera_tabela(numero,expression_1,expression,text2) :   # Function responsable by show true-tables

      table = []
     
      if numero == "2" :

          table.append(["0","0",str(calcula(expression_1))])
          expressao_mudada = muda_valor(expression,[0,1],text2)
          table.append(["0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0],text2)
          table.append(["1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1],text2)
          table.append(["1","1",str(calcula(expressao_mudada))])
          return table

      if numero == "3" :
        
          table.append(["0","0","0",str(calcula(expression_1))])
          expressao_mudada = muda_valor(expression,[0,0,1],text2)
          table.append(["0","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,0],text2)
          table.append(["0","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,1],text2)
          table.append(["0","1","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,0],text2)
          table.append(["1","0","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,1],text2)
          table.append(["1","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,0],text2)
          table.append(["1","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,1],text2)
          table.append(["1","1","1",str(calcula(expressao_mudada))])

          return table

      if numero == "4" :
        
          table.append(["0","0","0","0",str(calcula(expression_1))])
          expressao_mudada = muda_valor(expression,[0,0,0,1],text2)
          table.append(["0","0","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,0,1,0],text2)
          table.append(["0","0","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,0,1,1],text2)
          table.append(["0","0","1","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,0,0],text2)
          table.append(["0","1","0","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,0,1],text2)
          table.append(["0","1","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,1,0],text2)
          table.append(["0","1","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[0,1,1,1],text2)
          table.append(["0","1","1","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,0,0],text2)
          table.append(["1","0","0","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,0,1],text2)
          table.append(["1","0","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,1,0],text2)
          table.append(["1","0","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,0,1,1],text2)
          table.append(["1","0","1","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,0,0],text2)
          table.append(["1","1","0","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,0,1],text2)
          table.append(["1","1","0","1",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,1,0],text2)
          table.append(["1","1","1","0",str(calcula(expressao_mudada))])
          expressao_mudada = muda_valor(expression,[1,1,1,1],text2)
          table.append(["1","1","1","1",str(calcula(expressao_mudada))])

          return table

    def muda_valor(expression,lista_values,text2) :
           
            value_d = 0
            value_c = 0
            value_b = 0
            value_a = 0

            cont=0
      
            for i in text2 :
              if i == "A" : value_a = lista_values[cont]
              elif i == "B" : value_b = lista_values[cont]
              elif i == "C" : value_c = lista_values[cont]
              elif i == "D" : value_d = lista_values[cont]
              cont+=1
            
            expression_1 = []
            for i in expression :
              if i == "A" : expression_1.append(value_a)
              elif i == "B" : expression_1.append(value_b)
              elif i == "C" : expression_1.append(value_c)
              elif i == "D" : expression_1.append(value_d)
              else : expression_1.append(i)
           
            return expression_1

    def importa_expressao_booleana() :
                
                expression = expressao_url
                text_2 = []

                for i in expression :
                  if i in 'ABCDE' and i not in text_2:
                      text_2 += i

                variaveis = len(text_2)
                value_d = 0
                value_c = 0
                value_b = 0
                value_a = 0
                expression_1 = []

                for i in expression :
                  if i == "A" : expression_1.append(value_a)
                  elif i == "B" : expression_1.append(value_b)
                  elif i == "C" : expression_1.append(value_c)
                  elif i == "D" : expression_1.append(value_d)
                  else : expression_1.append(i)
                
                resposta = gera_tabela(str(variaveis),expression_1,expression,sorted(text_2))

                return resposta


    def funcao_principal() :

              exp = []
              exp = importa_expressao_booleana()
              return exp
    

    def conta_especial(exp1,indice) :        ## Realiza conta que tenham elementos especiais
            
              op = 1

              if '(' in exp1 and ')' in exp1 : aux = exp1[exp1.index('(')+1:exp1.index(')')]
              elif '[' in exp1 and ']' in exp1 : aux = exp1[exp1.index('[')+1:exp1.index(']')]
              elif '{' in exp1 and '}' in exp1 : aux = exp1[exp1.index('{')+1:exp1.index('}')]

              while(True) :

                  if '*' in aux : valor = operacoes_exp.multiplicar(exp1,indice,aux,op)
                  elif '+' in aux : valor = operacoes_exp.somar(exp1,indice,aux,op)
      
                  elif len(aux) == 1 : return(aux[0]) 

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

            op = 0


            while(True) :           ## Realiza a sequencia de operacoes
             
                if '*' in expressao : valor = operacoes_exp.multiplicar(expressao,1,1,op)
                elif '+' in expressao : valor = operacoes_exp.somar (expressao,1,1,op)
                elif len(expressao) == 1 : return(expressao[0]) 
    
    lista_tabela = funcao_principal()
    
    lista_letras = []

    for i in expressao_url :
      if i in "ABCDE" and i not in lista_letras:
        lista_letras.append(i)
   
    return render_template("tabela.html",rows=lista_tabela,numero=len(lista_letras),letras=sorted(lista_letras))
        

if __name__ == '__main__':
    app.run(debug=True)