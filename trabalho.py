import pandas as pd

tabela = pd.read_excel('TrabalhoAluno.xlsx')
print(tabela)
tabela['MÉDIA'] = (tabela['NOTA1'] + tabela['NOTA2']) / 2

tabela.loc[tabela['MÉDIA'] >= 6, 'SITUAÇÃO']= 'APROVADO'
tabela.loc[tabela['MÉDIA'] < 6, 'SITUAÇÃO']= 'REPROVADO'

print(tabela)

tabela.to_excel('TrabalhoAluno_Corrigido.xlsx', index=False)