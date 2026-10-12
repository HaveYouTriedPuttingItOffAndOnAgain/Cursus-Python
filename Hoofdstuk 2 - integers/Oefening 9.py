pe = float(input("De prijs per product exclusief btw: "))
a = int(input("Het aantal producten "))
pi = pe * 1.21
pt = pi * a
print("De totale prijs inclusief btw: €", round(pt, 2))