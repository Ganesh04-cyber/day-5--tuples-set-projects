shop_1_items = [("apple", 100), ("milk", 60), ("bread", 30)]
shop_2_items = [("apple", 90), ("milk", 70), ("eggs", 50)]


unique_items=set([item[0] for item in shop_1_items] +[item[0] for item in shop_2_items])
print(unique_items)

item1=set([item[0] for item in shop_1_items])
item2=set([item[0] for item in shop_2_items])
common_items=item1.intersection(item2)
print(common_items)
only2=item2.difference(item1)
print(only2)

expensive1=max(shop_1_items,key=lambda x:x[1])
expensive2=max(shop_2_items,key=lambda x:x[1])
print(f"expensive 1st shop",{expensive1[0]}-{expensive1[1]})
print(f"expensive in 2nd shop ",{expensive2[0]}-{expensive2[1]})
