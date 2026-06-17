"""
Crie na mão um pequeno CSV (usando o módulo nativo ou pelo Bloco de Notas)
contendo Aluno, Portugues, Matematica. Em seguida:

Use pd.read_csv para carregá-lo.
Crie uma coluna nova Media como a soma das duas dividida por 2.
Filtre na tela apenas os alunos com média >= 7
"""

import pandas as pd

df = pd.read_csv("notas.csv")

df["Media"] = (df["Portugues"] + df["Matematica"]) / 2

aprovados = df[df["Media"] >= 7]

print(aprovados)