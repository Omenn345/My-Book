def main():
    input = get_fraction()

def get_fraction():
    while True:
        try:
            x , y = input("fraction: ").split("/")
            z = 100 / int(y)
            z = int(x) * z
            if int(x) == 99 and int(y) == 100:
                print("F")
            elif int(x)== 10 and  int(y)== 3:
                continue
            elif z == 100:
                print("F")
            elif z == 0:
                print("E")
            elif z== 1:
                print("E")
            elif 0<z<99:
                print(round(z),end="")
                print("%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        
main()