menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
base = 0
while True:
    try:
        item = input("Item: ").title()
        base = base + menu[item]
        print(f"${base:.2f}")
    except EOFError:#################################     ctr d se program ends
        print()
        break
    except KeyError:
        pass

