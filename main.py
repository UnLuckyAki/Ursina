import timeit
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()
ground = Entity(model = 'plane',texture = 'grass',collider = 'mesh',scale = (100,1,100))

Sky()
player = FirstPersonController()

#myBox = Entity(model = 'cube',color = color.black,collider = 'box',position = (5, 0.5, 5))
#myBall = Entity(model = 'sphere',color = color.red,collider = 'sphere',position = (5, 0.5, 10))

blocks = []
directions = []
for i in range(8):
    r = uniform(-2,2)
    block = Entity(model='cube',
                   color=color.azure,
                   texture = 'white_cube',
                   position = (r,1,3+i*5),
                   scale=(3, 0.5,3),
                   collider = 'box')
    if r<0:
        directions.append(1)
    else:
        directions.append(-1)

    blocks.append(block)

def update():
    if player.y > 1:
        destroy(ground)
    i = 0
    for block in blocks:
        block.x -= directions[i]*time.dt
        if abs(block.x)>5:
            directions[i] *= -1
        i += 1
def input(key):
    if key == 'q':
        quit()
app.run()
