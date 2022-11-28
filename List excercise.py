drinks = ['coke', 'sprite', 'fanta', '7up']
print(drinks)
print(drinks[0])
print(drinks[0].title())
print(drinks[1])
print(drinks[3])
print(drinks[-1])
message = f"My favourate drink is {drinks[1].title()}."

print(message)
friends = ['kripa', 'delia','bhagya','aneesh']
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
message = f"Hello {friends[-1]}"
print(message)
message1 = f"Hello {friends[0]}"
print(message1)
friends.append('anjali')
print(friends)
friends.insert(0,'arun')
print(friends)
del friends[1]
print(friends)
for value in range(1, 5):
    print(value)
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
        print(squares)


bact = 500
for num in range (1,25):
    bact = bact*2
print(bact)
