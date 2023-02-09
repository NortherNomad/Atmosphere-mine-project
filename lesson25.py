# sandwich = ['Хлеб', 'Плесень', 'Масло', 'Майонез', 'Помидор', 'Сыр']
#
# for ingridient in sandwich:
#     if ingridient == 'Плесень':
#         print('Плесени место только в сыре, фу на такой сендвич')
#         break
#     else:
#         print(ingridient)
# else:
#     print('Вот и весь сендвич, конец законченного цикла')
# blocks = [
#           [35, 35, 22, 22, 22, 22, 35, 35],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 35, 35, 35, 35, 22],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 22, 22, 35, 35, 22],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [35, 35, 22, 22, 22, 22, 35, 35]
# ]
# print(blocks[0][1])
# for i in blocks:
#     for j in i:
#         print(j)


import random
randomNumbers = []
for outer in range(10):
    randomNumbers.append([])
    for inner in range(10):
        number = random.randint(0, 100)
        randomNumbers[outer].append(number)
print(randomNumbers)

# import random
# import keyboard
# import time
# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
# def rainbow_wall_generation(width:int=10, height:int=10):
#     randomColors = []
#
#     for array in range(width):
#         randomColors.append([])
#         for element in range(height):
#             number = random.randint(0, 15)
#             randomColors[array].append((35, number))
#     return randomColors
#
# def stone_wall_generation(width:int=10, height:int=10):
#     stoneBricks = []
#     brokenBricks = [(1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(1, 5), (1, 6), (7, 0)]
#
#     for array in range(width):
#         stoneBricks.append([])
#         for element in range(height):
#             stoneBricks[array].append(random.choice(brokenBricks))
#     return stoneBricks
#
# def generation(width1:int = 10, height1:int = 10):
#     x, y, z = mc.player.getTilePos()
#     y -= 1
#     blocks = []
#     print('Генерируем')
#
#     if keyboard.is_pressed('q'):
#         blocks = rainbow_wall_generation(width1, height1)
#     elif keyboard.is_pressed('p'):
#         blocks = stone_wall_generation(width1, height1)
#
#     start_x = x
#     for array in blocks:
#         for block in array:
#             mc.setBlock(x, y, z, block[0], block[1])
#             # time.sleep(0.05)
#             x += 1
#         z += 1
#         x = start_x
# if __name__ == '__main__':
#     while True:
#         generation(5, 5)
#         if keyboard.is_pressed('m'):
#             break

# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
# cube = [[[57, 57, 57, 57],
#          [57, 0, 0, 57],
#          [57, 0, 0, 57],
#          [57, 57, 57, 57]],
#
#         [[57, 0, 0, 57],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [57, 0, 0, 57]],
#
#         [[57, 0, 0, 57],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [57, 0, 0, 57]],
#
#         [[57, 57, 57, 57],
#          [57, 0, 0, 57],
#          [57, 0, 0, 57],
#          [57, 57, 57, 57]]]
# cube[0][3][0] = 89
# # print(cube)
# x, y, z = mc.player.getTilePos()
# for array in cube:
#     for array2 in array:
#         for block in array2:
#             mc.setBlock(x, y, z, block)
#             x += 1
#         z += 1
#         x -=4
#     y += 1
#     z -= 4

def sum(x1, x2):
    return x1 + x2

x = sum(1, 2)
print(1 + x)
# x = sum(1, 2)
