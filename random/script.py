from menu_item import MenuItem

menu_item1 = MenuItem("Roti Lapis", 5)
menu_item2 = MenuItem("Kue Coklat", 4)
menu_items = [menu_item1, menu_item2]

for menu_item in menu_items:
    print(menu_item.info())