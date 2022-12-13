"""
Exercice 4 :
Soit (Un) n?N une suite définie par récurrence. 
Écrire une script qui affiche U0, . . . U10 dans le cas suivant en utilisant
une boucle while : U0 = 1, et Un+1 = 2Un + 1
"""

u=0
n=0
while n<=10:
   u=2*u+1
   print("U",n," =",u)
   n+=1
