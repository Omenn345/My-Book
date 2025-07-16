#try:
#    x = int(input("X = "))
#    print(f"x is {x}") 
#except ValueError:
#    print("X is not int")

# x is 90 x = int
#x is not int  x = str

#try:
#    x = int(input("What's is x?: "))
#    print(f"x i s{x}")
#except ValueError:
#    a = int(input("type a int: "))
#    print(f"x is {a}")


#######################################################     1


#while True:
#   try:
#      x = int(input("What's x?"))
#      print(f"x is {x}")
#      break # if its a int then end
#   except ValueError:
#      print("x is not a int")

######################################################      2

#def main():
#    x = get_int()
#    print(f"x is {x}")

#
#def get_int():
#    while True:
#        try:
#            x = int(input("What's x?"))
#        except ValueError:
#            print("x is not an integer")
#        else:
#            return x # ye loop ko break as well as return the value of


#main()
#####################################################       3

#def main():
#    x = get_int("what's x: ")
#    print(f"x is {x}")

#def get_int(n):
#    while True:
#        try:
#            return int(input(n))
#        except ValueError:
#            pass
    
#main()

def main():
    input = get_fraction()

def get_fraction():
    while True:
        try:
            x , y = input("fraction: ").split("/")
            z = 100 / int(y)
            z = int(x) * z
            print(int(z),end="%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        
    

main()