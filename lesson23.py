# sandwich = ["Кусок хлеба", "Масло", "Тунец", "Лист салата", "Майонез", "Кусок хлеба"]
# for ingredient in sandwich:
#     if ingredient == "Майонез":
#         print("Не люблю сэндвичи с майонезом.")
#         break
#     else:
#         print(ingredient)
# else:
#     print("Вот и весь сэндвич.")

array = [3, 4, 5, 7, 9]
back_array = reversed(array)
print(list(back_array))

from mcpi.minecraft import Minecraft
import keyboard
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
def pyramid(block:int, height:int):
    x, y, z = mc.player.getTilePos()
    x, y, z = x+height, y, z

    color = 0

    for level in reversed(range(height)):
        if color > 15:
            color = 0
        mc.setBlocks(x-level, y, z-level, x+level, y, z+level, block, color)
        y += 1
        color += 1

while True:
    if keyboard.is_pressed('q'):
        pyramid(block=35, height=10)
    elif keyboard.is_pressed('m'):
        break


# mc.setBlock(x,y,z,35,0)

# sandwich = ["Кусок хлеба", "Масло", "Тунец", "Лист салата", "Майонез", "Кусок хлеба"]
# for i in sandwich:
#     print(i)

# string = 'text'

# for i in string:
#     print(i + ' буква из текста')

# inventory = {
#     "камни": 5,
#     "Зелья": 7,
#     "коробка": 1
# }
# for i in inventory:
#     print(i + ' ' + str(inventory[i]))


# from mcpi.minecraft import Minecraft
# import keyboard
# import random
# import time
# mc = Minecraft.create()
# x, y, z = mc.player.getTilePos()
# def pyramid(height:int):
#     x, y, z = mc.player.getTilePos()
#     x, y, z = x+height, y, z

#     for level in range(height):
#         block = random.randint(0, 100)
#         if block == 8 or block == 9 or block == 11 or block == 10:
#             block = random.randint(0, 100)
#         mc.setBlocks(x-level, y, z-level, x+level, y, z+level, block)
#         y += 1
#         time.sleep(1)

# while True:
#     if keyboard.is_pressed('q'):
#         pyramid(height=10)
#     elif keyboard.is_pressed('m'):
#         break

# ist = [i for i in range(10)]
# height = 4
# for i in range(height):
#     print(ist[i])
