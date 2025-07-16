#x = int(input("Number of blocks:"))#

#for _ in range(x):
#    print("#")#blocks

    #rows

#def main():
#    insert_row(3)

#def insert_row(width):
 #   print("#"*width, end = "\n")


#main()

                                       #squre 3 by 3

def main():
    dimention = get_side()
    insert_sq(dimention)

def get_side():#n = +ve
    while True:
        x = int(input("Side of sq:"))
        if x>0:
            break
    return x

def insert_sq(side):#side of sq
    for _ in range(side):
        print("#"*side)


main()




#def main():
#    print_square(3)


#def print_square(size):
#    for i in range(size):
#        print_row(size)


#def print_row(width):
#    print("#" * width)


#main()