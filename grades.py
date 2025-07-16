score = int(input("enter your percentages:"))
if score<= 100:
    x = score
    if x>= 90:
        print("Grade A")
    elif x<90 and x>=70:
        print("Grade B")
    elif 70 < x <= 50:
        print("Grade C")
    else:
        print("Grade E")
else:
    print("write again")


