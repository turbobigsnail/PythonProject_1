wtr = int(input("введите кол-во: "))
wtr = sum([wtr,wtr])
final_bonus = wtr + 20 * (wtr > 150)

print(f"Магическая сила зелья: {final_bonus}")