"""
Ngulang Materi Sekuensial dan Percabangan
"""

#1. Sekuensial

print('Mom said, “Ndut, go to Bude shop.”')
print('Ndut replied, “what for mom?”')
print('Mom replied “Go to the shop to buy a liter of coconut oil, if there is any rice buy 5')
print('Ndut went to Bude shop')
print('Ndut looking for coconut oil')
print('Ndut makes sure he bring enough money')
print('Ndut go home and give it to mom')

#2. Percabangan

bottle_of_coconut_oil = 100
bag_of_rice = 10

print(f'bottle_of_coconut_oil {bottle_of_coconut_oil} Ltr')
print(f'bag_of_rice {bag_of_rice} Kg')

if bottle_of_coconut_oil > 0:
    print('Ndut makes sure he bring enough money')
    if bag_of_rice > 0:
        print('Ndut bought 5 Ltr')
        print('Ndut buy 1 Kg')
    else:
        print('Ndut bought 1 Ltr')
print('Ndut go home and give the grocery to mom')
