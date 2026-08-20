leviskat = float(input("leiviskät:"))
naulat = float(input("naulat:"))
luodit = float(input("luodit:"))
kaikki= leviskat * 20 * 32 + naulat * 32 + luodit

grammat = kaikki * 13.3
kilot = int(grammat // 1000)
loput_grammat = grammat % 1000

print("Massa nykymittojen mukan:")
print(f"{kilot} kilogrammaa ja {loput_grammat:.2f} gramma.")