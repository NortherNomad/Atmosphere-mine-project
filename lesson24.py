# oneDimensionalList = [
#     0,
#     1,
#     2,
#     3,
#     4
# ]
# for i in oneDimensionalList:
#     print(i)
# blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 35, 35, 35, 35, 22],
#           [22, 35, 22, 35, 35, 22, 35, 22],
#           [22, 35, 35, 22, 22, 35, 35, 22],
#           [35, 22, 35, 35, 35, 35, 22, 35],
#           [35, 35, 22, 22, 22, 22, 35, 35]]
# for row in reversed(blocks):
#     print(row)

# import time
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# x, y, z = mc.player.getTilePos()


# w = 35
# g = 41
# wy = 165
# c = 173

# three_d = [
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
#     [
#         [0, 41, 41, 41, 41, 41, 41, 0],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [0, 41, 41, 41, 41, 41, 41, 0],
#     ],
#     [
#         [0, 41, 41, 41, 41, 41, 41, 0],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [0, 41, 41, 41, 41, 41, 41, 0],
#     ],
#     [
#         [41, 41, 41, 41, 41, 41, 41, 41],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [41, 41, wy, wy, wy, wy, 41, 41],
#         [41, 41, 41, 41, 41, 41, 41, 41],
#     ],
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
#     [
#         [0, 0, 41, 41, 41, 41, 0, 0],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, wy, wy, wy, wy, 41],
#         [41, wy, c, wy, wy, c, wy, 41],
#         [41, wy, wy, c, c, wy, wy, 41],
#         [0, 41, wy, wy, wy, wy, 41, 0],
#         [0, 0, 41, 41, 41, 41, 0, 0],
#     ],
# ]

# start_x = x
# start_y = y
# start_z = z

# for two_d in reversed(three_d):
#     for one_d in reversed(two_d):
#         for element in one_d:
#             mc.setBlock(x, y, z, element)
#             time.sleep(0.1)
#             x += 1
#         y += 1
#         x = start_x
#     y = start_y
#     z += 1
# z = start_z


# listOneDimension = [
#     0,
#     1,
#     2,
#     3,
#     4,
#     5
# ]

# print(listOneDimension[0])

# listTwoDimension = [
#     [0, 1, 2, 3],
#     [0, 1, 2, 4, 5, 6, 7]
# ]
# # 0
# print(listTwoDimension[0])

# listTwoDimension = [
#     [0, 1, 2, 3],
#     [0, 1, 2, 4, 5, 6, 7]
#     ]
# print(listTwoDimension[1])
# # listOfColors = [0, 1, 2, 3, 4, 5]

# # from mcpi.minecraft import Minecraft
# # mc = Minecraft.create()
# # x, y, z = mc.player.getTilePos()
# # for i in listOfColors:
# #     mc.setBlock(x, y, z, 35, i)
# #     z += 1
# twoDimensionalRainbowList = [
#                              [0, 0, 0],
#                              [1, 1, 1],
#                              [2, 2, 2],
#                              [3, 3, 3],
#                              [4, 4, 4],
#                              [5, 5, 5]
#                              ]
# print('!!!!!!!!!!!!!')
# for i in twoDimensionalRainbowList:
#     # print(i)
#     for element in i:
#         print(element)
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# twoDimensionalRainbowList = [
#                              [0, 0, 0],
#                              [1, 1, 1],
#                              [2, 2, 2],
#                              [3, 3, 3],
#                              [4, 4, 4],
#                              [5, 5, 5]
#                              ]

# x, y, z = mc.player.getPos()

# startingX = x
# for row in twoDimensionalRainbowList:
#     for color in row:
#         mc.setBlock(x, y, z, 35, color)
#         x += 1
#     y += 1
#     x = startingX


# twoDimensionalRainbowList = [
#                              [0, 0, 0],
#                              [1, 1, 1],
#                              [2, 2, 2],
#                              [3, 3, 3],
#                              [4, 4, 4],
#                              [5, 5, 5]
#                              ]

# for i in twoDimensionalRainbowList:
#     for element in i:
#         print(element + 1)


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]

# for row in reversed(blocks):
#     for block in row:
#         mc.setBlock(x, y, z, block)
#         # mc.postToChat('asdasd')
#         x += 1
#     y += 1
#     x = pos.x

izum = 133
brown = 35, 12
# tree = [
#         [0, 0, 0, 0, 0, 133, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 133, 133, 133, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 133, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 133, 133, 133, 0, 0, 0, 0, 0],
#         [0, 0, 0, 133, 133, 133, 133, 133, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0]
#         ]

# for i in reversed(tree):
#     for block in i:
#         if block == 35:
#             mc.setBlock(x, y, z, block, 12)    
#         else:
#             mc.setBlock(x, y, z, block)
#         x += 1
#     y += 1
#     x = pos.x

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()


w = 35
g = 41
wy = 165
c = 173

three_d = [
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
    [
        [0, 41, 41, 41, 41, 41, 41, 0],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [0, 41, 41, 41, 41, 41, 41, 0],
    ],
    [
        [0, 41, 41, 41, 41, 41, 41, 0],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [0, 41, 41, 41, 41, 41, 41, 0],
    ],
    [
        [41, 41, 41, 41, 41, 41, 41, 41],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [41, 41, wy, wy, wy, wy, 41, 41],
        [41, 41, 41, 41, 41, 41, 41, 41],
    ],
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
    [
        [0, 0, 41, 41, 41, 41, 0, 0],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, wy, wy, wy, wy, 41],
        [41, wy, c, wy, wy, c, wy, 41],
        [41, wy, wy, c, c, wy, wy, 41],
        [0, 41, wy, wy, wy, wy, 41, 0],
        [0, 0, 41, 41, 41, 41, 0, 0],
    ],
]

start_x = x
start_y = y
start_z = z

for two_d in reversed(three_d):
    for one_d in reversed(two_d):
        for element in one_d:
            mc.setBlock(x, y, z, element)
            time.sleep(0.1)
            x += 1
        y += 1
        x = start_x
    y = start_y
    z += 1
z = start_z