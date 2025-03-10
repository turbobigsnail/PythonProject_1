from collections import Counter

goods = "папайя:14,яблоко:10,банан:5,яблоко:7,апельсин:3,папайя:88"
goods_list = goods.split(",")
goods_list = [good.split(":") for good in goods_list]

goods_dict = Counter()
for key, value in goods_list:
   goods_dict[key] += int(value)

dict(goods_dict)

print(goods_dict)