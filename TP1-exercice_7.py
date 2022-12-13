"""
Exercice 7 :
Soit L une liste de nombres. Calculer la somme des carrés des éléments de L en utilisant la 
notion de List-comprehensions. 
Par exemple, si L=[0,1,2], on doit obtenir 5
"""
l=[i**2 for i in range(1,11)]
s=0
for i in range(10):
    s=s+l[i]
print("la somme des carrés des éléments de L est :",s)
