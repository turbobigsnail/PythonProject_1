herbs = int(input("введите кол-во травы: "))
cristals = int(input("введите кол-во кристаллов: "))
pepper_dust = int(input("введите кол-во 'огненной пыли': "))
moonshine = int(input("введите кол-во 'лунного света': "))
water = int(input("введите кол-во воды: "))

total = sum([herbs * 0.5, cristals * 1.5, pepper_dust * 1.0, moonshine * 1.2, water * 0.8])
bonus = total + ((total > 150) * 20)

print("Магическая сила зелья:", bonus)