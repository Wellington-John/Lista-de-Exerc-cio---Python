pares = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} <<<<PAR")
        pares += 1
    else:
        print(i)
print(f"Quantida de números pares: {pares}")


