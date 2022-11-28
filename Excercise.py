# A = int(input("Enter number of minutes:"))
# B = 60
# C = A/B
# print(C)

A = int(input("Enter the distance between LA and sydney : "))
B = int(input("Speed of the aircraft: "))
C = A/B
print("Length of the flight time : ",C)

#Set
D = set([1,2,3,4,5,6])
E = set(['a','b','c','d','e','f',1,2])
print(D | E) # Union
print(D&E) # Intersection

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed


tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[2:5])