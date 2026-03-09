print("🩸Cadastro de doadores de sangue🩸")

nome = input("👨‍🦲Insira seu nome: ")
peso = float(input("⚖️Insira seu Peso(Em Kg):"))
altura = int(input("🦒Insira sua altura(Em cm):"))
ano_nascimento = int(input("📝Insira seu Ano de Nascimento: "))

idade = 2026 - ano_nascimento
peso_minimo = peso > 50
idade_minima = idade >=16

texto_saida = f"\n\t👨‍🦲NOME: {nome}\n\t⚖PESO: {peso} kg\n\t🦒ALTURA: {altura} cm\n\t📝IDADE: {idade} Anos\n\t❓POSSUI O PESO MINIMO PARA ENTRAR: {peso_minimo}\n\t❔TEM IDADE MINIMA PARA DOAR: {idade_minima}"
print(texto_saida)