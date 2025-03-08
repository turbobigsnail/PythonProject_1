herbs = int(input("введите кол-во травы: "))
cristals = int(input("введите кол-во кристаллов: "))
pepper_dust = int(input("введите кол-во 'огненной пыли': "))
moonshine = int(input("введите кол-во 'лунного света': "))
water = int(input("введите кол-во воды: "))

magic_power = (herbs * 0.5 + cristals * 1.5 + water * 0.8 + pepper_dust * 1.0 + moonshine * 1.2)
magic_power_rounded = round(magic_power, 2)
#
total = sum([herbs, cristals, pepper_dust, moonshine, water])
bonus = total + ((total > 150) * 20)

print("Магическая сила зелья:", bonus)