xd = {"Mleko":"2zł",
"Ser": "3zł",
"soja": "200zł","złoto":"sztuki","diamenty":"sztuki"}
#odwrocone = {value: key for key, value in xd.items()}
g={ key for key , value in xd.items() if value=="sztuki" }
print("sklep")
print(xd)
print("sztuki")
print(g)