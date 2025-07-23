txt = " h\te\tl\tl\to"
#x= txt.expandtabs(2)
#print(x)

# h  e l l o

txt1 = "For only {price:.2f} dollars! "
txt2 = "For only {size:.2f} dollars!"
#print(txt1.format(price = 49))#For only 49.00 dollars!
#print(txt1.format(price = 80))#For only 80.00 dollars!
#print(txt2.format(size = 40))#For only 40.00 dollars!

txt3 = "My name is {name}, I'm {age}".format(name = "John", age = 36)
txt4 = "hi my name is random {laugh}, i am {emotion}" .format(laugh = " hehehheh", emotion = "sorry")
txt5 = "My name is {}, I'm {}".format("John",36)# specify karna no imp order wise chalta hai

##print(txt3)
#print(txt4)
#print(txt5)

txt6 = "Hello, welcome to my world."

#x = txt6.index(",")#uski location dega
#y = txt6.index("e",5 , 10)#"," jo 5 hai and 10th tak e kaha///////counting normak hi rahegi///
#print(x)
#print(y)

name = input("whats your name= ")
print ("hello " + name)