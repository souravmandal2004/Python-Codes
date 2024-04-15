'''
Object Types / Data Types:
1. Number
2. String
3. List: [1, 2, 3, 4, 5]
4. Tuple: (1, 2, 3, 4, 5)
5. Dictionary: {1: "one", 2: "two", 3: "three"}
6. Set: {1, 2, 3, 4, 5}
7. Boolean: True, False
8. None
9. Functions
10. Classes
11. Modules
12. Packages
13. Avance: Decorators, Generatos, Iterators, MetaProgramming

'''

myDictionary = {
    1: "Sourav",
    2: "Mandal"
}

print(myDictionary[1])


l1 = [1, 2, 3]
l2 = l1  # l2 takes the reference of l1
print (l1, l2)

h1 = [1, 2, 3]
h2 = h1[:]

print (h1, h2)  #h2 is a copy of h1 