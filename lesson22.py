ramen = ['noodles', 'oil', 'beef', 'garlic', 'pepper']

for ingridient in ramen:
    print(ingridient)
print('Конец программы')

for i in range(0, 101):
    print(str(i) + ' ' + str(i**2) + ' ' + str(i**3))

# from mcpi.minecraft import Minecraft
# import keyboard
# import time
# mc = Minecraft.create()
# time.sleep(5)
# hits = mc.events.pollBlockHits()
# gold = 41
#
# for hit in hits:
#     x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
#     mc.setBlock(x, y, z, gold)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import keyboard
x, y, z = mc.player.getTilePos()
y -=1
stairblock = 53
size = 50
for step in range(size):
    step += 1
    mc.setBlock(x+step, y+step, z, stairblock)
mc.postToChat('Построили листницу ура, пошли чай пить')

def builtStair(block_type: int = 53, size: int = 50):
    x, y, z = mc.player.getTilePos()
    y -= 1
    for step in range(size):
        step += 1
        mc.setBlock(x, y + step, z + step, stairblock)
    mc.postToChat('Построили листницу ура, пошли чай пить')

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('q'):
            builtStair()
        if keyboard.is_pressed('p'):
            break
