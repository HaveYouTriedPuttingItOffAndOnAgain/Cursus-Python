pr = input("Wat hebben jullie gekocht? ")
apr = int(input("Hoeveel hebben jullie er gekocht? "))
ape = int(input("Met hoeveel zijn jullie? "))
appe = apr/ape
rest = apr // ape
print("Elke persoon krijgt", round(appe,0), pr)
print("Er zijn", f"{rest}", pr, "rest")