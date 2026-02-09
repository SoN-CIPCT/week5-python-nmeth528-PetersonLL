birds = ["Asian Green Bee-eater", "Asian Koel", "Black Kite", "Collared Kingfisher", "Common Myna", "Indian Peafowl"]
print(*birds, sep= ", ")
print("The first two items in the list are: " + ', '.join(birds[0:2]))
print("The middle two birds in the list are: " + ', '.join(birds[2:4]))
print("The first and last items in the list are: " + ', '.join([birds[0], birds[-1]]))

menu = ('noodle', 'green onion', 'egg', 'mushroom', 'meatball')
for item in menu:
    print(item)
menu_list = list(menu)
menu_list[0] = 'rice'
menu_list[4] = 'tofu'
menu = tuple(menu_list)
print(menu)
for item in menu:
    print(item)