# Calcular a média de cada aluno;
# Exibir os alunos aprovados e reprovados (média >= 6 para aprovação);
# Permitir salvar um novo arquivo Excel com uma coluna adicional chamada “Situação” (Aprovado/Reprovado).
# O usuário deve escolher o nome do arquivo de saída no console.

# INSTALE A BIBLIOTECA PANDAS
import pandas as pd

#LER A PLANILHA
df = pd.read_excel("TrabalhoAluno.xlsx")

print("\n--- PLANILHA ORIGINAL ---")
print(df.to_string(index=False))
print("--------------------------\n")

#CÁLCULO DA MÉDIA
df["MÉDIA"] = df[["NOTA1", "NOTA2"]].mean(axis=1)

#SITUAÇÃO
df.loc[df["MÉDIA"] >= 6, "SITUAÇÃO"] = "APROVADO"
df.loc[df["MÉDIA"] < 6, "SITUAÇÃO"] = "REPROVADO"

#MOSTRAR RESULTADO FINAL
print("--- PLANILHA FINAL ---")
print(df.to_string(index=False))
print("-----------------------\n")

#SALVAR
nome = input("Nome do arquivo de saída (sem extensão): ").strip()
df.to_excel(f"{nome}.xlsx", index=False)

print("Arquivo salvo com sucesso!")