num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

operacao = input("Qual operação quer fazer?(+, -, /, *)")

if (operacao == "+"):
  print(num1+num2)
elif (operacao == "-"):
  print(num1-num2)
elif (operacao == "/"):
  print(num1/num2)
elif (operacao == "*"):
  print(num1*num2)
