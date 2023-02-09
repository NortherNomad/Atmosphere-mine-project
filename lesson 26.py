# 10: int
# 10.5: float
# 'asdasd': str
# [0, 1, 2, 'asdasdas', True, False, [0, 1321321, 54654, 'asdasd']] - list
# {'age': 38,
#  'name': 'Vasya'} - dict
# (23, 45, 56) - tuple
# True, False: bool
# {0, 1, 4, 5, 6} - set
# print(type({0, 1}))
# {'age': 38,
#  'name': 'Vasya'}
# print(set({0, 1, 2, 3, 2}))
# print(None)
# print(type(None))
# def nothing()->int:
#     return 2
#
# if nothing() is None:
#     print(1)

# def calculator(x, y):
#     print(x+y)
#
# x = calculator(1, 2)
#
# print(x)

# massive = [0, 1, 2, 4, 6, 5, 7, 8]
# massive.append(5)
# massive.insert(4, 100000)
# print(massive)

# slovar = {
#     'age': 38,
#     'name': 'Vasya'
# }
#
# x = 1, 2, 3, 4
# print(x, type(x))
#
# x = 1, 2, 3, 4, 5
# print(x, type(x))
#
# x = {0, 1, 4, 5, 6, 6}

# print(x)
# x.add(123132)
# print(x)
# x.pop()
# print(x)


# dict - изменяемый
# set - изменяемый
# massive - изменяемый
# typle - неизменяемый

# x = {0, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7}
#
# x.add(45)
# x.pop()
# print(x)

# slovar = {
#     'age': 36,
#     'name': 'Vasya',
#     'ownCar': True,
#     'goToschool': False
# }
# slovar['Mansur'] = 'Красавчик'
# print(slovar)

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
#
# def sortPair(val1, val2):
#     if val1 > val2:
#         return val2, val1
#     else:
#         return val1, val2
#
#
# def copyStructure(x1, y1, z1, x2, y2, z2):
#     # Получаем максимальные и минимальные значения x, y и z
#     x1, x2 = sortPair(x1, x2)
#     y1, y2 = sortPair(y1, y2)
#     z1, z2 = sortPair(z1, z2)
#
#     width = x2 - x1
#     height = y2 - y1
#     length = z2 - z1
#
#     structure = []
#     print("Пожалуйста, подождите…")
#
#     # Копируем блоки
#     for y in range(height):
#         structure.append([])
#         for z in range(length):
#             structure[y].append([])
#             for x in range(width):
#                 structure[y][z].append(mc.getBlock(x1 + x, y1 + y, z1 + z))
#
#     return structure
#
#
# def buildStructure():
#
#     # Получаем координаты первого угла
#     input("Пройдите к первому углу и нажмите Enter в этом окне")
#     pos = mc.player.getTilePos()
#     x1, y1, z1 = pos.x, pos.y, pos.z
#     # Получаем координаты второго (противоположного) угла
#
#     input("Пройдите к противоположному углу и нажмите Enter в этом окне")
#     pos = mc.player.getTilePos()
#     x2, y2, z2 = pos.x, pos.y, pos.z
#
#     # Копируем конструкцию
#     structure = copyStructure(x1, y1, z1, x2, y2, z2)
#     # Задаем координаты копии
#     input("Перейдите туда, где вы хотите создать конструкцию, ← и нажмите Enter в этом окне")
#     pos = mc.player.getTilePos()
#     x, y, z = pos.x, pos.y, pos.z
#
#     xStart = x
#     yStart = y
#     zStart = z
#     for y in range(len(structure)):
#         for z in range(len(structure[y])):
#             for x in range(len(structure[y][z])):
#                 mc.setBlock(x + xStart, y + yStart, z +
#                             zStart, structure[y][z][x])
#
#
# buildStructure()



# slovar = {
#     'name': 'Grisha',
#     'age': 8,
#     'goToSchool': True,
# }
#
# slovar.pop('age')
# print(slovar)
# slovar['age'] = True
# print(slovar)
# slovar['ownCar'] = False
# #
# # print(slovar)
#
# number: int = 10
# number: float = 10.0
# message: str = "Hello"
# is_active: bool = True
# numbers: list = [1, 2, 3]
# numbers: tuple = (1, 2, 3)
# numbers: set = {1, 2, 3}
# vocablure: dict = {"one": 1, "two": 2, "three": 3}
# types: type = type(1)
# nothing: None = None
#
# # Динамическая типизация
# # Статическая типизация
#
# # def sum(x, y):
# #     print(x+y)
#
# # sum('asdasdasd', 'asdasd')
# # print('a'+1)
# # java, javascript
# # print(int('1'))
# print(int(True))
# print(int(False))
#
