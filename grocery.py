basket= {

}
while True:
    try:
        item = input().title().upper()
        if item not in basket:
            basket[item] = 1
        else:
            basket[item] = basket[item] + 1
    except EOFError:
        dict = dict(sorted(list(basket.items())))
        for item in dict:
            print(dict[item],item)
        break
    except KeyError:
        continue