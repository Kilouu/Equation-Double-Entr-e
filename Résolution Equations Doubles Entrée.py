# Programme réaliser par Naashy
# Date : 18/03/2020
# Résolution de 2 Equations à 2 Inconnues
# ax + by = c
# dx + ey = f

# Entrez les Valeurs de A, B, C, D, E et F

print("Résolution de 2 Equations à 2 Inconnues : ", end ="")
print("ax + by = c ", end = "")
print("ET ", end = "")
print("dx + ey = f")
print("Entrez les Valeurs de A, B, C, D, E et F")
A = eval(input("Entrez A : "))
B = eval(input("Entrez B : "))
C = eval(input("Entrez C : "))
D = eval(input("Entrez D : "))
E = eval(input("Entrez E : "))
F = eval(input("Entrez F : "))

print("Voici l'équation n°1 : " ,A,"x + ",B,"y = ",C)
print("Voici l'équation n°2 : " ,D,"x + ",E,"y = ",F)

# Test qui indique si le système admet une solution

if (A*E-B*D) == 0:
    print("Le système n'admet pas de solution.")


# Calcule et écriture des 2 Solutions

else:
    print("Le système admet 2 Solutions : ")
    print("X = ", ((C*E-B*F)/(A*E-B*D)))
    print("Y = ", ((A*F-C*D)/(A*E-B*D)))

# Fin ©
# My GitHub : https://github.com/Naashy
# My Discord : Naashy#8434
# Devoir Lycée
