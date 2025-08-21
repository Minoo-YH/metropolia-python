# 1 leiviskä = 20 naulaa; 1 naula = 32 luotia; 1 luoti = 13.3 g
leiviskat = float(input("Anna leiviskät: "))
naulat   = float(input("Anna naulat: "))
luodit   = float(input("Anna luodit: "))
total_grams = ((leiviskat * 20 + naulat) * 32 + luodit) * 13.3
kg = int(total_grams // 1000)
grams = total_grams - kg * 1000
print("\nMassa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {grams:.2f} grammaa.")
