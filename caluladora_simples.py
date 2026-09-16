# CALCULADORA

def calculadora():
    print("Calculadora Simples")
    print("Operações: +, -, *, /")

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
            return

        print(f"Resultado:R$ {resultado}")

    except ValueError:
        print("Erro: insira apenas números válidos.")


calculadora()
