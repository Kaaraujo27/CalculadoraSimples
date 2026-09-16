# CALCULADORA SIMPLES
# Atualizado com WHILE ao invés de ser somente IF, ELIF ou ELSE.

def calculadora():
    print("Calculadora Simples")
    print("Operações: +, -, *, /")
    continuar = "s"

    while continuar == "s":
        try:
            primeiro = float(input("Primeiro número:R$ "))
            operacao = input("Operação: ").strip()
            segundo = float(input("Segundo número:R$ "))

            if operacao == "+":
                resultado = primeiro + segundo
            elif operacao == "-":
                resultado = primeiro - segundo
            elif operacao == "*":
                resultado = primeiro * segundo
            elif operacao == "/":
                if segundo == 0:
                    print("Erro: não é possível dividir por zero.")
                    return
                resultado = primeiro / segundo
            else:
                print("Operação inválida.")
                continue

            print(f"Resultado:R$ {resultado}")
        except ValueError:
            print("Erro: informe números válidos.")

        continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()

calculadora()
