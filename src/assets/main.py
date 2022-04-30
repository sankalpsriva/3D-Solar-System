from ursina import *
import numpy as np
import math


def input(key):
    global pause
    letters = ["z","x","c","b","l","k","h","y","q"]
    if key == "1":
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, 0, -60)
        camera.rotation_x = 0

    if key == "2":
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, defaultHeight, 0)
        camera.rotation_x = 90

    if key == "escape":
        pause = not pause
        
# m, v, e, ma, j, 
# z = Mercury, x = Venus, c = Earth, b = Mars (r), l = Jupiter, k = Saturn, h = Uranus, y = Neptune, q = Pluto 

    if key == "m":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["z"] = 1

    if key == "v":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["x"] = 1

    if key == "e":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["c"] = 1

    if key == "r":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["b"] = 1

    if key == "j":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["l"] = 1

    if key == "s":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["k"] = 1

    if key == "u":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["h"] = 1

    if key == "n":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["y"] = 1

    if key == "p":
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["q"] = 1

def update():
    global mercuryDeltaT, venusDeltaT, earthDeltaT, marsDeltaT, jupiterDeltaT, saturnDeltaT, uranusDeltaT, neptuneDeltaT, plutoDeltaT, cameraDeltaT
    global mercury_radius, venus_radius, earth_radius, mars_radius, jupiter_radius, saturn_radius, uranus_radius, neptune_radius, pluto_radius
    global pause

    if not pause:
        mercuryDeltaT += 0.212 / speedDiv # 0.02
        venusDeltaT += 0.185 / speedDiv  # 0.03
        earthDeltaT += 0.15 / speedDiv  # 0.034
        marsDeltaT += 0.1 /  speedDiv  # 0.0415
        jupiterDeltaT += 0.07 / speedDiv
        saturnDeltaT += 0.0415 / speedDiv # 0.1
        uranusDeltaT += 0.034 / speedDiv# 0.15
        neptuneDeltaT += 0.03 / speedDiv# 0.185
        plutoDeltaT += 0.02 / speedDiv # 0.212
        cameraDeltaT += 0.02

        mercury_radius = 1.8
        mercury.x = math.cos(mercuryDeltaT) * mercury_radius
        mercury.z = math.sin(mercuryDeltaT) * mercury_radius
        mercury.rotation_y += time.dt * 50

        venus_radius = 3
        venus.x = math.cos(venusDeltaT) * venus_radius
        venus.z = math.sin(venusDeltaT) * venus_radius
        venus.rotation_y += time.dt * 50


        earth_radius = 4.4
        earth.x = math.cos(earthDeltaT) * earth_radius
        earth.z = math.sin(earthDeltaT) * earth_radius
        earth.rotation_y += time.dt * 50


        mars_radius = 5.8
        mars.x = math.cos(marsDeltaT) * mars_radius
        mars.z = math.sin(marsDeltaT) * mars_radius
        mars.rotation_y += time.dt * 50


        jupiter_radius = 8.3
        jupiter.x = math.cos(jupiterDeltaT) * jupiter_radius
        jupiter.z = math.sin(jupiterDeltaT) * jupiter_radius 
        jupiter.rotation_y += time.dt * 50


        saturn_radius = 12
        saturn.x = math.cos(saturnDeltaT) * saturn_radius
        saturn.z = math.sin(saturnDeltaT) * saturn_radius
        saturn.rotation_y += time.dt * 50


        uranus_radius = 15
        uranus.x = math.cos(uranusDeltaT) * uranus_radius
        uranus.z = math.sin(uranusDeltaT) * uranus_radius
        uranus.rotation_y += time.dt * 50


        neptune_radius= 16.8
        neptune.x = math.cos(neptuneDeltaT) * neptune_radius
        neptune.z = math.sin(neptuneDeltaT) * neptune_radius
        neptune.rotation_y += time.dt * 50


        pluto_radius = 19
        pluto.x = math.cos(plutoDeltaT) * pluto_radius
        pluto.z = math.sin(plutoDeltaT) * pluto_radius
        pluto.rotation_y += time.dt * 50

        if held_keys["z"]:
            camera.x = math.cos(mercuryDeltaT) * mercury_radius
            camera.z = math.sin(mercuryDeltaT) * mercury_radius

        if held_keys["x"]:
            camera.x = math.cos(venusDeltaT) * venus_radius
            camera.z = math.sin(venusDeltaT) * venus_radius

        if held_keys["c"]:
            camera.x = math.cos(earthDeltaT) * earth_radius
            camera.z = math.sin(earthDeltaT) * earth_radius

        if held_keys["b"]:
            camera.x = math.cos(marsDeltaT) * mars_radius
            camera.z = math.sin(marsDeltaT) * mars_radius

        if held_keys["l"]:
            camera.x = math.cos(jupiterDeltaT) * jupiter_radius
            camera.z = math.sin(jupiterDeltaT) * jupiter_radius

        if held_keys["k"]:
            camera.x = math.cos(saturnDeltaT) * saturn_radius
            camera.z = math.sin(saturnDeltaT) * saturn_radius

        if held_keys["h"]:
            camera.x = math.cos(uranusDeltaT) * uranus_radius
            camera.z = math.sin(uranusDeltaT) * uranus_radius

        if held_keys["y"]:
            camera.x = math.cos(neptuneDeltaT) * neptune_radius
            camera.z = math.sin(neptuneDeltaT) * neptune_radius

        if held_keys["q"]:
            camera.x = math.cos(plutoDeltaT) * pluto_radius
            camera.z = math.sin(plutoDeltaT) * pluto_radius

    if held_keys["up arrow"]:
        camera.y -= .5

    if held_keys["down arrow"]:
        camera.y += .5

    if held_keys["left arrow"]:
        camera.x -= .5

    if held_keys["right arrow"]:
        camera.x += .5

    if held_keys["shift"]:
        if held_keys["up arrow"]:
            camera.z += .5

    if held_keys["shift"]:
        if held_keys["down arrow"]:
            camera.z -= .5

    

app = Ursina()

defaultHeight = 100
speedDiv = 5
state3 = False


sun = Entity(model = "sphere", scale = 2, texture = "sun.png")
mercury = Entity(model = "sphere", scale = .8, texture = "mercury.jpg")
venus = Entity(model = "sphere", scale = .9, texture = "venus.jpg")
earth = Entity(model = "sphere", scale = 1, texture = "earth.jfif")
mars = Entity(model = "sphere", scale = .7, texture = "mars.png")
jupiter = Entity(model = "sphere", scale = 3, texture = "jupiter.jpg")
saturn = Entity(model = "sphere", scale = 2.5, texture = "saturn.jpg")
neptune = Entity(model = "sphere", scale = 1.2, texture = "neptune.jpg")
uranus = Entity(model = "sphere", scale = 1.5, texture = "uranus.jfif")
pluto = Entity(model = "sphere", scale = .5, texture = "pluto.jpg")

# pluto = Entity(model = "sphere", color = color.pink, scale = .3)

camera.position = (0, defaultHeight, 0)
camera.rotation_x = 90

pause = False

Sky(texture = "download.jfif")

mercuryDeltaT = np.pi
venusDeltaT = np.pi
earthDeltaT = np.pi
marsDeltaT = np.pi
jupiterDeltaT = np.pi
saturnDeltaT = np.pi
uranusDeltaT = np.pi
neptuneDeltaT = np.pi
plutoDeltaT = np.pi
cameraDeltaT = np.pi


app.run()