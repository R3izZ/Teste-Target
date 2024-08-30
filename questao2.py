def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False


numero = 21 

if is_fibonacci(numero):
    print(f"{numero} pertence a sequencia de Fibonacci.")
else:
    print(f"{numero} não pertence a sequencia de Fibonacci.")
