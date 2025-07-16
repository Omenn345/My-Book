x = input("Input:")
v = ["a","e","i","o","u"]
print("Output:", end="")
for _ in x:
    if _.casefold() not in v:
        print(_, end="")


print()

#####removing leters
