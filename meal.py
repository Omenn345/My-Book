def main():
    x = input("What time is it?: ")
    convert(x)


def convert(time):
    a, b = time.split(":")
    h = int(a)
    n = int(b)
    m = float(n / 60)
    if h>12:
        l = float(h - 12)
        t = float(l+m)
        if t>=0 and t<= 1:
            print("Lunch time")
        elif t>=6 and t<= 7:
            print("Dinner time")
    elif h <= 12:
        p = h +m
        if p >=7 and p<= 8:
            print("Breakfast time")
        elif p == 12:
            print("lunch time")
    else:
        print(" ")

if __name__ == "__main__":
    main()