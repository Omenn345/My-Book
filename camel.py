Given = input("camelCase: ")
print("snake_case: ", end="")

for word in Given:
    if word.islower():
        print(word, end="")
    elif word.isupper():
        print("_", word.lower(), end="", sep="")

print()


#newww
#islower
#isupper
