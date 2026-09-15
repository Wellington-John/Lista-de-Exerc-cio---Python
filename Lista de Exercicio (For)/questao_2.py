number = int(input("Digite um número: "))

print("----Adição----")
for i in range(11):
    soma = number + i
    print(f"{number}+{i} = {soma}")

print("\n----Subtração----")
for i in range(11):
    sub = number - i
    print(f"{number}-{i} = {sub}")

print("\n----Multiplicação----")
for i in range(11):
    mult = number * i
    print(f"{number}*{i} = {mult}")

print("\n----Divisão----")
for i in range(1, 11):
    div = number / i
    print(f"{number}/{i} = {div}")

