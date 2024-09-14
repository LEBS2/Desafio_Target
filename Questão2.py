def pertence_fibonacci(n):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Enquanto o número 'a' for menor ou igual ao número informado
    while a <= n:
        if a == n:  # Se 'a' for igual ao número, significa que ele pertence à sequência
            return True
        a, b = b, a + b  # Atualiza os valores de 'a' e 'b' com os próximos números da sequência
    
    return False  # Se o loop terminar e 'a' não for igual ao número, ele não pertence à sequência

# Entrada do número
num = int(input("Informe um número: "))

# Verifica se o número informado pertence à sequência de Fibonacci
if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
