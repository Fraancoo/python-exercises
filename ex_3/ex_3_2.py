char = input("Ingrese un carácter: ")
vowels = 'aeiou'
abc = 'abcdefghijklmnopqrstuvwxyz'

print(char + " es una vocal: " + str(vowels.find(char) >= 0))
print(char + " es una letra minúscula: " + str(abc.find(char) >= 0))
print(char + " es un símbolo del alfabeto: " + str(abc.find(char) >= 0))
