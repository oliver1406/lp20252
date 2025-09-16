'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

HOJE = datetime.now() # Pega data/hora do computador

def cabecalho(titulo):
    print('========================================')
    print(f'============= {titulo} ===============')
    print('========================================')

def exemploSe():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')

def exemploSeSenao():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')    
    else:
        print('Menor de idade')
    print('fim do programa')

def exemploSe_SenaoSe_Senao():
    idade = int(input('Idade:'))
    if idade < 18:
        print('Menor de idade')    
    elif idade < 65:
        print('Maior de idade')
    elif idade < 50:
        print('Pessoa madura')
    else:
        print('Idoso')
    print('fim do programa')
    
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    n1 = int(input('Insira o primeiro numero: '))
    n2 = int(input('Insira o segundo numero: '))
    soma = n1+n2
    if soma > 10:
        print(soma)
    else:
     print("Soma menor que 10")
#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    n1= int(input("Digite o primeiro número: "))
    n2= int(input("Digite o segundo número: "))
    soma = n1+n2
    if soma> 20:
        print(soma+8)
    else :
        print(soma-5)

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num = int(input("Digite um número: "))
    if (num % 3 == 1):
        print("É multiplo de 3!")
    else:
        print("Não é multiplo de 3!")
#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num= int(input("Digite um número: "))
    if num%5 == 1:
        print("Divisível por 5")
    else:
        print("Não divisível por 5")
#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num= int(input("Digite um número: "))
    if num % 3 and num % 7:
        print("É divisivel")
    else:
        print("Não é divisivel")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = float(input("Sálario bruto: "))
    prestacao = float(input("Prestação para autorizar: R$: "))
    prestamax = salario * 0.3
    if prestacao > prestamax:
        print("Empréstimo não autorizado")
    else:
        print("Emprestimo autorizado")
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num = int(input("Digite um número: "))
    if num>=20 and num<=50:
        print("Está alocado entre 20 e 50")
    else:
        print("Não esta alocado")
#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num = int(input("Digite um número: "))
    if num > 20:
        print("Maior que 20")
    elif num < 20:
        print("Menor que 20")
    else:
        print("É igual a 20")
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    anonascimento = int(input("Digite seu ano de nascimento: "))
    anoatual = int(input("Digite o ano atual: "))
    if anonascimento > anoatual:
        print("Viagem no tempo????")
    else:
        print(f'Idade: {anoatual - anonascimento} anos')

def q91():
    data_str = input('Data de nascimento (dd/mm/aaaa): ')
    print(f'Ano atual: {datetime.strftime(HOJE,"%Y")}')
    data_nascimento = datetime.strptime(data_str, '%d/%m/%Y')
    if data_nascimento > HOJE:
        print('Data de nascimento inválida!')
    else:
        print(f'Idade: {int((HOJE - data_nascimento).days/365)} anos.')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    numeros = [n1,n2,n3]
    numeros.sort()
    print(numeros)

#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    if n1 > n2 and n3:
        print(n1)
    elif n2 > n1 and n3:
        print(n2)
    else:
        print(n3)

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
    idade = int(input("Informe sua idade: "))
    if idade >= 18 and idade < 65:
        print("Maior de idade")
    elif idade < 18:
        print("Menor de idade")
    else: 
        print("Idoso")
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    nome = str(input("Qual o seu nome?: "))
    n1 = int(input("Nota prova 1: "))
    n2 = int(input("Nota prova 2: "))
    media = (n1 + n2)/2
    print("Aluno: ",nome)
    print("Nota 1: ",n1)
    print("Nota 2: ",n2)
    print("Sua média: ",media)
    if media >=7:
        print("Aprovado")
    elif media <7 and media >3:
        print("Em Prova final")
    else:
        print("Reprovado")
#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input("Digite seu salário: "))
    if salario > 600 and salario <= 1200:
        desconto=(salario*20)/100
    elif salario > 1200 and salario <= 2000:
        desconto = (salario*25)/100
    elif salario > 2000:
        desconto =  (salario*30)/100
    else:
        desconto = 0
    print("Salario bruto: ",salario)
    print("Desconto do INSS: ",desconto)
    print("Salario liquido: ", salario-desconto)

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    compra = int(input("Qual o valor da compra? "))
    if compra <= 20:
        venda=(compra*45)/100
    else:
         venda=(compra*30)/100
    print("Valor da venda será de: ",venda+compra)

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input("Digite sua idade: "))
    if idade<=7:
        print("Categoria Infantil [A]")
    elif idade >=8 and idade <=10:
        print("Categoria Infantil [B]")
    elif idade >=11 and idade <=13:
        print("Categoria Juvenil [A]")
    elif idade >=14 and idade<=17:
        print("Categoria Juvenil [B]")
    elif idade >= 18:
        print("Categoria Sênior")


#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    if idade<=10:
        valor=30
    elif idade>10 and idade<=29:
        valor=60
    elif idade>29 and idade<=45:
        valor=120
    elif idade>45 and idade<=59:
        valor=150
    elif idade>59 and idade<=65:
        valor=250
    elif idade>65:
        valor=400
    print(nome,"o valor de seu plano de saúde é de: ",valor)



#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    num = int(input("Digite um número do mês: "))
    if num == 1:
        print("Seu número corresponde ao mês de Janeiro")
    elif num ==2:
        print("Seu número corresponde ao mês de Fevereiro")
    elif num ==3:
        print("Seu número corresponde ao mês de Março")
    elif num ==4:
        print("Seu número corresponde ao mês de Abril")
    elif num ==5:
        print("Seu número corresponde ao mês de Março")
    elif num ==6:
        print("Seu número corresponde ao mês de Junho")
    elif num ==7:
        print("Seu número corresponde ao mês de Julho")
    elif num ==8:
        print("Seu número corresponde ao mês de Agosto")
    elif num ==9:
        print("Seu número corresponde ao mês de Setembro")
    elif num ==10:
        print("Seu número corresponde ao mês de Outubro")
    elif num ==11:
        print("Seu número corresponde ao mês de Novembro")
    elif num ==12:
        print("Seu número corresponde ao mês de Dezembro")
    else:
        print("Número inválido")




#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    prato = input('Prato(vegetariano/peixe/frango/carne): ')
    calorias = 0
    calorias +=180 if prato == "vegetariano" else 0
    calorias +=230 if prato == "peixe" else 0
    calorias +=250 if prato == "frango" else 0
    calorias +=350 if prato == "carne" else 0
    sobremesa = input('sobremesa: (abacaxi/sorvete diet/mousse diet/mousse chocolate): ')
    calorias +=75 if sobremesa == "abacaxi" else 0
    calorias +=110 if sobremesa == "sorvete diet" else 0
    calorias +=170 if sobremesa == "mousse diet" else 0
    calorias +=200 if sobremesa == "mousse chocolate" else 0
    bebida = input('bebida: (chá/suco de laranja/suco de melão/refrigerante diet): ')
    calorias +=20 if bebida == "chá" else 0
    calorias +=70 if bebida == "suco de laranja" else 0
    calorias +=100 if bebida == "suco de melão" else 0
    calorias +=65 if bebida == "refrigerante diet" else 0

    print(f'Total de calorias do pedido: {calorias} cal')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
