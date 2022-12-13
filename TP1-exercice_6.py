"""
Exercice 6 :
Soit une liste de nombres. Trouver le plus grand élément de cette liste sans
utiliser la fonction prédéfinie max
"""

L=[]
n=int(input("Saisir le nombre des éléments :"))
for i in range(n):
   print("Entrer le l'élément ",i+1,":",end="")
   x=int(input())
   L.append(x)

Max=L[0]
for i in range(n):
   if L[i]>Max:
      Max=L[i]

print("le plus grand élément de cette liste est :",Max)
