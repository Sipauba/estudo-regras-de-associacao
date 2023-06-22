import csv
from apyori import apriori

# Definir os parâmetros para a análise de relações
min_support = 0.002  # Suporte mínimo
min_confidence = 0.005  # Confiança mínima
min_lift = 1.0  # Lift mínimo
min_length = 2  # Comprimento mínimo

# Ler os dados do arquivo CSV
dados = []
with open('mercado2.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        # Remover os espaços em branco e dividir a linha por vírgulas
        pedido = [produto.strip() for produto in linha if produto.strip() and len(produto.strip()) >= min_length]
        dados.append(pedido)

# Executar a análise de relações
resultado = list(apriori(dados, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift))

# Exibir os resultados
for item in resultado:
    # Obter os itens antecedentes
    itens_antecedentes = [list(elemento) for elemento in item[2][0][0]]
    
    # Obter os itens consequentes
    itens_consequentes = [list(elemento) for elemento in item[2][0][1]]
    
    # Obter o suporte, confiança e lift
    suporte = item[1]
    confianca = item[2][0][2]
    lift = item[2][0][3]
    
    # Exibir a relação encontrada
    print(f"Itens antecedentes: {itens_antecedentes}")
    print(f"Itens consequentes: {itens_consequentes}")
    print(f"Suporte: {suporte}")
    print(f"Confiança: {confianca}")
    print(f"Lift: {lift}")
    print()
