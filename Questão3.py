import json

# Função para carregar o faturamento de um arquivo JSON
def carregar_faturamento_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        faturamento_diario = json.load(f)
    return faturamento_diario

# Função para calcular os dados solicitados
def calcular_faturamento(faturamento_diario):
    # Filtrando os dias com faturamento (ignorando dias com valor 0)
    faturamento_validos = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]
    
    if len(faturamento_validos) == 0:
        return None, None, 0
    
    # Calculando o menor e o maior faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    
    # Calculando a média mensal
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)
    
    # Contando o número de dias com faturamento acima da média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)
    
    # Retornando os resultados
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Caminho do arquivo JSON
caminho_arquivo = 'C:\\Users\PC\\OneDrive\Documentos\\faturamento.json.json'

# Carregar os dados de faturamento do arquivo JSON
faturamento_diario = carregar_faturamento_json(caminho_arquivo)

# Calculando e exibindo os resultados
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

if menor is not None and maior is not None:
    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima}")
else:
    print("Nenhum faturamento válido foi encontrado.")
