from ursina import *
import numpy as np
import math
def update():
    global increment
    global deltaT
    deltaT = deltaT + .02

    mercury_radius = 1.65
    mercury.x = math.cos(deltaT) * mercury_radius
    mercury.z = math.sin(deltaT) * mercury_radius

    venus_radius = 3
    venus.x = math.cos(deltaT) * venus_radius
    venus.z = math.sin(deltaT) * venus_radius

    earth_radius = 4.4
    earth.x = math.cos(deltaT) * earth_radius
    earth.z = math.sin(deltaT) * earth_radius

    mars_radius= 5.8
    mars.x = math.cos(deltaT) * mars_radius
    mars.z = math.sin(deltaT) * mars_radius

    jupiter_radius= 8.3
    jupiter.x = math.cos(deltaT) * jupiter_radius
    jupiter.z = math.sin(deltaT) * jupiter_radius

    saturn_radius= 11
    saturn.x = math.cos(deltaT) * saturn_radius
    saturn.z = math.sin(deltaT) * saturn_radius

    neptune_radius= 12.5
    neptune.x = math.cos(deltaT) * neptune_radius
    neptune.z = math.sin(deltaT) * neptune_radius

    uranus_radius= 14.7
    uranus.x = math.cos(deltaT) * uranus_radius
    uranus.z = math.sin(deltaT) * uranus_radius



    if increment % 500 == 0:
        camera.position = (x, 0, -40)
        camera.rotation = 0
    if increment % 1500 == 0:
        camera.position = (0, defaultHeight, 0)
        camera.rotation = 90


    increment += 1
    print(increment)

app = Ursina()

defaultHeight = 80
sun = Entity(model = "sphere", color = color.yellow,  scale = 2)
mercury = Entity(model = "sphere", color = color.gray, scale = .8)
venus = Entity(model = "sphere", color = color.green, scale = .9)
earth = Entity(model = "sphere", color = color.blue, scale = 1)
mars = Entity(model = "sphere", color = color.red, scale = .7)
jupiter = Entity(model = "sphere", color = color.orange, scale = 3)
saturn = Entity(model = "sphere", color = color.gold, scale = 1.13)
neptune = Entity(model = "sphere", color = color.blue, scale = 1.2)
uranus = Entity(model = "sphere", color = color.pink, scale = 1.5)

skybox_image = load_texture(r"ursina-project\ursina-project\assets\images\download.jfif")
Sky(texture = skybox_image)
# pluto = Entity(model = "sphere", color = color.pink, scale = .3)


x = 0
camera.position = (0, defaultHeight, 0)
increment = 0

deltaT = np.pi
app.run()

