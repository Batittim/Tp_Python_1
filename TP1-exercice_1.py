"""
Exercice 1 :
Soit L une liste de nombres. Calculer la somme des éléments de L, puis le nombre d’éléments 
de L et en déduire la moyenne arithmétique des éléments de L. 
Par exemple, si L=[0,1,2,3], on doit obtenir 1.5

"""


L=[]
n=int(input("Saisir le nombre des notes :"))
s=0
for i in range(n):
   x=float(input("Entrer les notes :"))
   L.append(x)
   s+=x
   
m=s/len(L)
print("La moyenne de votre notes est :",m)

