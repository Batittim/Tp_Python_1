"""
Exercice 5 :
Quel résultat donne le code suivant ? Après avoir écrit la réponse,
vérifiez-là avec l’ordinateur.
"""
L1 = list(range(0,11,2)) 
L2 = list(range(1,12,2)) 
L = []
for i in range(len(L1)):
   L= L + [L1[i]] + [L2[i]]
print("L1=",L1)
print("L2=",L2)
print("L=",L)

###############OUTPUT#####################
"""

L1= [0, 2, 4, 6, 8, 10]
L2= [1, 3, 5, 7, 9, 11]
L= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Ce script fait la concaténation entre les élements du list L1 et les élements du list L2 :
L=[L1[0],L2[0],L1[1],L2[2],.....,L1[12],L2[12]]

"""
