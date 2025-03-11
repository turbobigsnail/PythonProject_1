goods = "папайя:14,яблоко:10,банан:10,яблоко:27,апельсин:3,папайя:88"
goods_list = goods.split(",")
goods_list = [good.split(":") for good in goods_list]
#goods_dict = {2:3}
goods_dict = {}

for k , value in goods_list:
  goods_dict[k] = goods_dict.get(k, 0) + int(value)

print(goods_dict)