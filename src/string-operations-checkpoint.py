name = "Michael Jackson"

print(name)


### SLICING

print(name[0:4])

print(name[8:12])

Numbers="0123456"
print(Numbers[::2])


### STRIDE

# select every 2nd variable
print(name[::2])

# select every 3rd variable
print(name[::3])

# select every 2nd variable for 1st 5 chars
print(name[0:5:2])


### TUPLES: Slicing

print(len(name))


### CONCATENATE

print(name + " is the best!")


### REPLICATE string value

print(3 * name)


### STRING ESCAPE SEQUENCE

print(name + " \n was the best!")

print(name + " \t was the best!")

print(name + " \\ was the best!")

print(r"What does the r means?")


### METHOD: upper

print(name.upper())


### METHOD: replace

decision = name + " is the best"
print(decision.replace('Michael', 'Janet'))


### STRIDE

print(name.find('el'))

print(name.find('Jack'))

print(name.find('jack'))

print("0123456".find('1'))
