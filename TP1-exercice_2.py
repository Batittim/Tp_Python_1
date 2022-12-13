"""
Exercice 2 :
Soit L une liste de nombres entiers donnés. Soit n un élément dans L. Calculer 
l’effectif et la fréquence de n dans cette liste. 
Par exemple, si L=[0,10,20,10,20,30,20,30,40,20], et n = 20 alors son effectif est 4 
(nombre de fois où il apparaît) et sa fréquence est 4/10 (effectif de la valeur / effectif total).

"""



L=[]
n=int(input("Saisir le nombre des éléments :"))
for i in range(n):
   print("Entrer le l'élément ",i+1,":",end="")
   x=int(input())
   L.append(x)
y=int(input("entrer un nombre à calculer son effectif et sa fréquence :"))
cpt=0
for i in range(n):
   if L[i]==y:
      cpt+=1
print("l’effectif de ",y," dans cette liste est :",cpt)
print("la fréquence de ",y," dans cette liste est :",cpt/len(L))
