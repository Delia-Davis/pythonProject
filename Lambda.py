calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(13))

x = lambda a : a + 10
n = int(input("Enter the number:"))
print(x(n))

def myfunc(n):
  return lambda a : a * n
z = int(input("Enter the number to double"))
mydoubler = myfunc(2)

print(mydoubler(z))