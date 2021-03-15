xd = {"Mleko":"2zł",
"Ser": "3zł",
"soja": "200zł","złoto":"sztuki","diamenty":"sztuki"}
g={ key for key , value in xd.items() if value=="sztuki" }
print("sklep")
print(xd)
print("sztuki")
print(g)