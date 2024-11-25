#programme affichant chif de 0 à 20
for number in range (21):
    print(number)
#programme affichant chif de 0 à 20 - chif 1 sur 2
for i in range (21):
    if i % 2 == 0:
        print(i)
#programme affichant les multiplications
N = int(input("Veuillez entrer un entier N supérieur à zéro : "))
if N > 0:
    for i in range(1, N+1):
        print(f"La table de multiplication de {i} :")
        for j in range(1, 11):
            print(f"{i} X {j} = {i * j}")
        print()
else:
    print("Veuillez entrer un nombre supérieur à zéro")

#mettre programme avec while
N = int(input("Entrez un entier N supérieur à zéro : "))
if N > 0:
    i = 0
    while i <= N:
        print(f"Table de multiplication de {i} :")
        for j in range(1, 11):
            print(f"{i} X {j} = {i * j}")
        print()

        i += 1

else:
    print("Veuillez entrer un nombre supérieur à zéro.")

#programme affichant les premiers résultats de la multiplications par N * 7
N = int(input(f"Entrez un entier N supérieur à zéro :"))
i = 1
while i <= 10:
    print(f"{N} X {i} X 7 = {N * i * 7}")
    i += 1

#boucle 12 tours - 2
# Boucle de 12 tours
for tour in range(1, 13):
    resultat = 3 * tour - 2
    print(f"Tour {tour} : {resultat}")


#Boucle de 12 tours avec numéro précédent +2
# Initialisation de la variable precedent
precedent = 0

# Boucle de 12 tours
for tour in range(1, 13):
    precedent += 2
    print(f"Tour {tour} : {precedent}")
   





        

    
    
