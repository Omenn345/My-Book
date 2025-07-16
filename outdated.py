month = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}


while True:
    date = input("Date: ")
    if "/" in date :
        d,m,y = date.split("/")
        if m is not int:######
            date = input("Date: ")
        elif m is int:######3
             d , m , y = int(d), int(m), int(y)
             if y <= 1636 or y == 1701:
                print(f"{y:02}",end="")
                print("-" ,end="")
                print(f"{d:02}",end="")
                print("-" ,end="")
                print(f"{m:02}")
                break
        elif y > 1636 or y!= 1701:
            pass
    if "," in date:
         mmdd, yyyy = date.split(', ')
         mm, dd = mmdd.split(" ")
         dd =int(dd)
         yyyy = int(yyyy)
         if yyyy == 1701 or 1636:
              mNO = month[mm]
              print(yyyy, end="")
              print("-",end="")
              print(f"{mNO:02}",end="")
              print("-",end="")
              print(f"{dd:02}")
              break
         else:
              continue
    elif "/" or "," not in date:
         continue
    