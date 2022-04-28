from ursina import *
from random import randint
def update():
    # global x, speed
    # x = x + time.dt * speed
    # cube.x = cube.x + time.dt * .5
    # red  = randint(0,255)
    # # blue = randint(0,255)
    # # green = randint(0,255)
    # # cube.color = color.rgb(red, green, blue)
    for i in cubes:    
        i.rotation_x += time.dt * 100
        i.rotation_y += time.dt * 100
    # if abs(x) > 3:
    #     speed = speed * -1
    # camera.position = (x, 0, -20)
app = Ursina()

cubes = []

# Model = "cube", "circle", "quad", "sphere"                                        color.rgb(r, g ,b)
cube = Entity(model = "cube", color = color.yellow,  rotation = (45, 45, 0), texture = "white_cube")
cube2 = Entity(model = "cube", color = color.yellow, rotation = (45, 45, 0), position = (2,0,0), texture = "brick")
cube3 = Entity(model = "cube", color = color.yellow, rotation = (45, 45, 0), position = (-2,0,0), texture = "radial_gradient")
cube4 = Entity(model = "cube", color = color.yellow, rotation = (45, 45, 0), position = (0,2,0), texture = "sky_sunset")
cube5 = Entity(model = "cube", color = color.yellow, rotation = (45, 45, 0), position = (0,-2,0), texture = "horizontal_gradient")

cubes.append(cube)
cubes.append(cube2)
cubes.append(cube3)
cubes.append(cube4)
cubes.append(cube5)
x = 0
speed = 1
txt = Text(text = "this is a red cube", x = .3, y = .3)

app.run()