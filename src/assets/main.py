from ursina import *
import numpy as np
import math
from colorama import Fore, Back, Style


def input(key):
    global pause, controls
    letters = ["z","x","c","b","l","k","t","y","q"]
    
    # Keyboard Presses
    if key == "1": # Camera posistion one, side view of planets
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, 0, -70)
        camera.rotation_x = 0

    if key == "2": # Camera posistion two, bird's eye view 
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, defaultHeight, 0)
        camera.rotation_x = 90

    if key == "escape": # Pauses movement
        pause = not pause
    
    if key == "h": # Prints controls to the terminal 
        print(" ")
        for key in controls.keys():
            print(f"{Fore.GREEN + key}: {Fore.GREEN + controls[key]} {Fore.WHITE}")

    if key == "m": # Follows Mercury
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["z"] = 1

    if key == "v": # Follows Venus
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["x"] = 1

    if key == "e": # Follows Earth
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["c"] = 1

    if key == "r": # Follows Mars
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["b"] = 1

    if key == "j": # Follows Jupiter
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["l"] = 1

    if key == "s": # Follows Saturn
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["k"] = 1

    if key == "u": # Follows Uranus
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["t"] = 1

    if key == "n": # Follows Neptune
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["y"] = 1

    if key == "p": # Follows Pluto
        camera.y = 20
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys["q"] = 1

def update(): 
    # Global variables that are used, cannot be defined here because it would never increase
    global mercuryDeltaT, venusDeltaT, earthDeltaT, marsDeltaT, jupiterDeltaT, saturnDeltaT, uranusDeltaT, neptuneDeltaT, plutoDeltaT, cameraDeltaT
    # global mercury_radius, venus_radius, earth_radius, mars_radius, jupiter_radius, saturn_radius, uranus_radius, neptune_radius, pluto_radius
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
        plutoDeltaT += 0.015 / speedDiv # 0.212
        cameraDeltaT += 0.02

        sun.rotation_y += time.dt * 20

        mercury_radius = 2.3
        mercury.x = math.cos(mercuryDeltaT) * mercury_radius
        mercury.z = math.sin(mercuryDeltaT) * mercury_radius
        mercury.rotation_y += time.dt * 50

        venus_radius = 3.5
        venus.x = math.cos(venusDeltaT) * venus_radius
        venus.z = math.sin(venusDeltaT) * venus_radius
        venus.rotation_y += time.dt * 50


        earth_radius = 5
        earth.x = math.cos(earthDeltaT) * earth_radius
        earth.z = math.sin(earthDeltaT) * earth_radius
        earth.rotation_y += time.dt * 50

        moon.y = .5
        moon.x = math.cos(earthDeltaT) * (earth_radius - 4) + earth.x
        moon.z = math.sin(earthDeltaT) * (earth_radius - 4) + earth.z
        moon.rotation_y += time.dt * 50


        mars_radius = 8
        mars.x = math.cos(marsDeltaT) * mars_radius
        mars.z = math.sin(marsDeltaT) * mars_radius
        mars.rotation_y += time.dt * 50


        jupiter_radius = 11
        jupiter.x = math.cos(jupiterDeltaT) * jupiter_radius
        jupiter.z = math.sin(jupiterDeltaT) * jupiter_radius 
        jupiter.rotation_y += time.dt * 50


        saturn_radius = 17
        saturn.x = math.cos(saturnDeltaT) * saturn_radius
        saturn.z = math.sin(saturnDeltaT) * saturn_radius
        saturn.rotation_y += time.dt * 50


        uranus_radius = 22
        uranus.x = math.cos(uranusDeltaT) * uranus_radius
        uranus.z = math.sin(uranusDeltaT) * uranus_radius
        uranus.rotation_y += time.dt * 50


        neptune_radius = 25
        neptune.x = math.cos(neptuneDeltaT) * neptune_radius
        neptune.z = math.sin(neptuneDeltaT) * neptune_radius
        neptune.rotation_y += time.dt * 50


        pluto_radius = 27
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

        if held_keys["t"]:
            camera.x = math.cos(uranusDeltaT) * uranus_radius
            camera.z = math.sin(uranusDeltaT) * uranus_radius

        if held_keys["y"]:
            camera.x = math.cos(neptuneDeltaT) * neptune_radius
            camera.z = math.sin(neptuneDeltaT) * neptune_radius

        if held_keys["q"]:
            camera.x = math.cos(plutoDeltaT) * pluto_radius
            camera.z = math.sin(plutoDeltaT) * pluto_radius

    if held_keys["up arrow"] and not held_keys["shift"]:
        camera.y += .5

    if held_keys["down arrow"] and not held_keys["shift"]:
        camera.y -= .5
    
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

app = Ursina(position = (0, 0))

defaultHeight = 143
speedDiv = 5


sun = Entity(model = "sphere", scale = 2, texture = "sun.png")
mercury = Entity(model = "sphere", scale = .8, texture = "mercury.jpg")
venus = Entity(model = "sphere", scale = .9, texture = "venus.jpg")
earth = Entity(model = "sphere", scale = 1, texture = "earth.jfif")
moon = Entity(model = "sphere", scale = .3, texture = "moon.jpg")
mars = Entity(model = "sphere", scale = .7, texture = "mars.png")
jupiter = Entity(model = "sphere", scale = 3, texture = "jupiter.jpg")
saturn = Entity(model = "sphere", scale = 2.5, texture = "saturn.jpg")
neptune = Entity(model = "sphere", scale = 1.2, texture = "neptune.jpg")
uranus = Entity(model = "sphere", scale = 1.5, texture = "uranus.jfif")
pluto = Entity(model = "sphere", scale = .5, texture = "pluto.jpg")


ring = Entity(model=load_model('torus.obj'))
ring.position = saturn.position
ring.scale = saturn.scale
ring.scale_y = .4
ring.rotation_x = 3
ring.reparent_to(saturn)
ring.color = color.rgb(159, 144, 114)

stars_radius = 500
for i in range(1000):
    star = Entity(model = "sphere", scale = .8, color = color.white, texture = "sky_sunset")
    bStar = Entity(model = "sphere", scale = .4, color = color.white, texture = "sky_sunset")

    star.x = math.cos(i) * stars_radius
    star.y = random.randint(-100, 100)
    star.z = math.sin(i) * stars_radius

    bStar.x = random.randint(-100, 100)
    bStar.y = -50
    bStar.z = random.randint(-100, 100)

    bStar.color = color.rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    star.color = color.rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    

uRing = Entity(model=load_model('torus.obj'))
uRing.position = uranus.position
uRing.scale = uranus.scale - .1
uRing.scale_y = .3
uRing.rotation_x = 110
uRing.reparent_to(uranus)
uRing.color = color.rgb(28, 156, 195)


# pluto = Entity(model = "sphere", color = color.pink, scale = .3)

camera.position = (0, defaultHeight, 0)
camera.rotation_x = 90

pause = False

Sky(texture = "download.jfif")

print(Fore.GREEN + "\nPress H For Controls\n" + Fore.WHITE)

controls = {
    "1": "3D View of Planets",
    "2": "Bird's Eye View of Solar System",
    "p": "Pauses movement",
    "m": "Follows Mercury",
    "v": "Folows Venus",
    "e": "Follows Venus",
    "r": "Follows Mars",
    "j": "Follows Jupiter",
    "s": "Follows Saturn",
    "u": "Follows Uranus",
    "n": "Follows Neuptune",
    "p": "Follows Pluto",
    "up arrow": "zooms out (up on y-axis)",
    "down arrow": "zooms in (down on y-axis)",
    "left arrow": "moves to the left",
    "right arrow": "moves to the right",
    "shift + left": "moves on the z-axis (on the sun's axis) closer to the sun",
    "shift + right": "moves on the z-axis (on the sun's axis) away from the sun"
}

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
