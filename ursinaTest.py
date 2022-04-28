from ursina import *
from random import randint
def update():
    global x, speed
    x = x + time.dt * speed
    # cube.x = cube.x + time.dt * .5
    # red  = randint(0,255)
    # # blue = randint(0,255)
    # # green = randint(0,255)
    # # cube.color = color.rgb(red, green, blue)
    # cube.rotation.x = cube.rotation.x + time.dt * 100
    # cube.rotation.y = cube.rotation.y + time.dt * 100
    if abs(x) > 3:
        speed = speed * -1
    camera.position = (x, 0, -20)
app = Ursina()

# Model = "cube", "circle", "quad", "sphere"                                        color.rgb(r, g ,b)
cube = Entity(model = "cube", color = color.rgb(255, 0, 0), scale = (1, 2, 5))

x = 0
speed = 1
txt = Text(text = "this is a red cube", x = .3, y = .3)
camera.position = (0, 0, 0)

app.run()