studentes = ["Hanna Makei", "Clarck", "Stones", "Clara", "Jayson", "John", "Helenna", "Yasmin"]
cout = 0
for studente in studentes:
    print(studente)

print("\n--------------------")
for studente in studentes:
      if len(studente) > 6:
            cout += 1
            print(f">>>{studente}")

print(f"Quantidade de nomes que atendem esse criterio: {cout}")