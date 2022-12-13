"""
Exercice 3 :
En utilisant l’itérateur range, générer et afficher les listes suivantes : 
A = [2, 3, 4, 5, 6, 7, 8, 9] 
B = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90] 
C = [2, 4, 6, 8, 10 12 14 16 18 20 22 . . . , 48, 50] 
D = [1, 3, 5, 7, . . . , 47, 49]

"""

A=[i+1 for i in range(1,9)]
print(A)

B=[i*9 for i in range(1,11)]
print(B)   

C=[i+2 for i in range(0,50,2)]
print(C)

D=[i+2 for i in range(-1,49,2)]
print(D) 
