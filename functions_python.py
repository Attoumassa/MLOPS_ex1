# What is a function ?
""" A function is a book of code that only runs when it is called."""

def my_functions():
    print("Hello world")

# Appel de la fonction
my_functions()

# least difference
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(least_difference(1,10,100), least_difference(1,10,10), least_difference(5,6,7))

#dit bonjour à "nom"
def say_hi(nom):
    print("Hi",nom)
