a = int(input("Hoeveel neem je er? "))
a5 = a//5
pa5 = a5*4.6
pa = (a%5)*2.3
pt = pa + pa5
print("De prijs is €", round(pt, 2))