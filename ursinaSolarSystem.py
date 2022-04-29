from ursina import *
import numpy as np
import math

def update():
    global increment, mercuryDeltaT, venusDeltaT, earthDeltaT, marsDeltaT, jupiterDeltaT, saturnDeltaT, uranusDeltaT, neptuneDeltaT, plutoDeltaT 
    mercuryDeltaT += 0.212 / 2 # 0.02
    venusDeltaT += 0.185 / 2  # 0.03
    earthDeltaT += 0.15 / 2   # 0.034
    marsDeltaT += 0.1 / 2     # 0.0415
    jupiterDeltaT += 0.07 / 2 
    saturnDeltaT += 0.0415 / 2 # 0.1
    uranusDeltaT += 0.034 / 2 # 0.15
    neptuneDeltaT += 0.03 / 2 # 0.185
    plutoDeltaT += 0.02 / 2  # 0.212

    


    mercury_radius = 1.65
    mercury.x = math.cos(mercuryDeltaT) * mercury_radius
    mercury.z = math.sin(mercuryDeltaT) * mercury_radius

    venus_radius = 3
    venus.x = math.cos(venusDeltaT) * venus_radius
    venus.z = math.sin(venusDeltaT) * venus_radius

    earth_radius = 4.4
    earth.x = math.cos(earthDeltaT) * earth_radius
    earth.z = math.sin(earthDeltaT) * earth_radius

    mars_radius = 5.8
    mars.x = math.cos(marsDeltaT) * mars_radius
    mars.z = math.sin(marsDeltaT) * mars_radius

    jupiter_radius = 8.3
    jupiter.x = math.cos(jupiterDeltaT) * jupiter_radius
    jupiter.z = math.sin(jupiterDeltaT) * jupiter_radius 

    saturn_radius = 11
    saturn.x = math.cos(saturnDeltaT) * saturn_radius
    saturn.z = math.sin(saturnDeltaT) * saturn_radius


    uranus_radius = 12.5
    uranus.x = math.cos(uranusDeltaT) * uranus_radius
    uranus.z = math.sin(uranusDeltaT) * uranus_radius


    neptune_radius= 14.7
    neptune.x = math.cos(neptuneDeltaT) * neptune_radius
    neptune.z = math.sin(neptuneDeltaT) * neptune_radius

    pluto_radius = 17
    pluto.x = math.cos(plutoDeltaT) * pluto_radius
    pluto.z = math.sin(plutoDeltaT) * pluto_radius

    if increment % 500 == 0 and increment % 1000 != 0:
        camera.position = (x, 0, -40)
        camera.rotation = 0
    elif increment % 1000 == 0:
        camera.position = (0, defaultHeight, 0)
        camera.rotation = 90


    increment += 1
    print(increment)

app = Ursina()

defaultHeight = 80

sun = Entity(model = "sphere", color = color.yellow,  scale = 2, texture = "sun.png")
mercury = Entity(model = "sphere", color = color.gray, scale = .8)
venus = Entity(model = "sphere", color = color.green, scale = .9)
earth = Entity(model = "sphere", color = color.blue, scale = 1)
mars = Entity(model = "sphere", color = color.red, scale = .7)
jupiter = Entity(model = "sphere", color = color.orange, scale = 3)
saturn = Entity(model = "sphere", color = color.gold, scale = 1.13)
neptune = Entity(model = "sphere", color = color.blue, scale = 1.2)
uranus = Entity(model = "sphere", color = color.pink, scale = 1.5)
pluto = Entity(model = "sphere", color = color.rgb(255, 0, 255), scale = .5)

# pluto = Entity(model = "sphere", color = color.pink, scale = .3)


x = 0
camera.position = (0, defaultHeight, 0)
increment = 0

mercuryDeltaT = np.pi
venusDeltaT = np.pi
earthDeltaT = np.pi
marsDeltaT = np.pi
jupiterDeltaT = np.pi
saturnDeltaT = np.pi
uranusDeltaT = np.pi
neptuneDeltaT = np.pi
plutoDeltaT = np.pi

app.run()

