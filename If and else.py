s = input("Enter the statement:")
print(s.replace('!', ''))

import string
x = input("Enter the statement:")
x = x.translate(string.maketrans("",""), string.punctuation)
print(x)
print(string.punctuation)


x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
elif x == y:
    print("x is equal to y")