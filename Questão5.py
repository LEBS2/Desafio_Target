# Função para inverter uma string manualmente
def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# String de entrada (pode ser alterada ou ser recebida do usuário)
string = input("Digite uma string para inverter: ")

# Chamando a função e exibindo o resultado
resultado = inverter_string(string)
print(f'String invertida: {resultado}')
