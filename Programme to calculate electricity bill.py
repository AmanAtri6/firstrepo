a=int(input("Enter Your Units Consumption"))
if a<=50:
    print(2*a)
if a>50 and a<150:
    print(2.50*a)

if a>150 and a<250:
    print(5.25*a)

if a>250 and a<500:
    print(5.25*a)
else:
    print(7.10*a)

