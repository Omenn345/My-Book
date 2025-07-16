expression =input(" ")

x,y,z = expression.split(" ")

x = float(x)

z = float(z)

if y == "+":
    answer = x + z
    print(f"{answer:.1f}")
elif y == "-":
    if x >= z:
        answer = x - z
        print(f"{answer:.1f}")
    elif x <= z:
        answer = z - x
        print(f"-{answer:.1f}")
elif y == "*":
    answer = x*z
    print(f"{answer:.1f}")
elif y == "/":
    answer = x / z
    print(f"{answer:.1f}")














def main():
    x = input("What time is it?: ")
    convert(x)


def convert(time):
    hour, minute = time.split(":")
    a = int(hour)
    if a > 12:
        a == hour - 12
        hour = str(a)
        print(hour)
    elif a <= 12:
        hour = str(a)
        print(hour)
    print(minute)


if __name__ == "__main__":
    main()