# # Todos los elemntos d eun conjunto se encuentra en otro conjunto.
# a={1,2,7,3}
# b={3,4,5,0}
# c={3,1,7,2,4,5,6,8}
# print(b.issubset(c))
# ***********************Super conjunto todos los elementos de un conjunto contiene los elementos de otro*******************************
a={1,2,7,3}
b={3,4,5,0}
c= {3,1,7,2,4,5,6,8,0}
print(c.issuperset(b))
#******************************Conjuntos disconexo,conjuntos que no comparten ningun elemento entre si ***********************
a={1,2,7,3}
b={3,4,5,0}
c= {6,8,9}
print(a.isdisjoint(c))
print(b.isdisjoint(a))
#******************************Conjunto inmutable, es decir que no se puede cambiar sus elementos*****************************
a=frozenset({1,2,7,3})
a.add(4)
print(a)