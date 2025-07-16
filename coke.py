def main2():
    print("Amount Due:", end="")
    y = 50
    print(y)
    x = int(input("Insert Coin:"))
    a = x % 5
    if a == 0 and x < 30:
         y = y -x
         if y != 0:
              print("Amount Due:" , end="")
              print(y)
         elif y == 0:
              print("Charged Owed:" , end="")
              print(y)
    else:
         print("Amount Due:", end=" ")
         print(y)
############################################check50 cs50/problems/2022/python/coke
def main():
        print("Amount due:", end=" ")
        y = 50
        print(abs(y))
        while True:
            x = int(input(""))
            a = x % 5
            if a == 0 and x < 30:
                y = y -x
                if y != 0:
                     print("Amount due: ", end="")
                     print((y))
                else:
                 print("Amount Due: ", end="")
                 print((y))

            if y == 0:
              print("Change Owed: ", end="")
              print((0))
              break


main()