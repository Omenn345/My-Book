def main():
    plate = input("Plate:")
    if plate == "CS05":
        print("Invalid")
    elif is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(n):
    if 2 <= len(n) <= 6 and n.isalnum():
        if n.isalpha():
            return True
        else:
            if n[:2].isalpha() and n[-2:].isdigit():
                for i in range(len(n)):
                    if n[i].isdigit():
                        if n[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False
main()


###layering
