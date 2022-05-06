from ursina import *
from tkinter import * 
import json
import numpy as np
import math
from colorama import Fore

global root
root = Tk()

def input(key):
    global pause, controls, trackingCameraHeight

    trackingCameraHeight = 50
    letters = ["z","x","c","b","l","k","t","y","q"]
    
    # Keyboard Presses
    if key == "1": # Camera posistion one, side view of planets
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, 0, -70)
        camera.rotation = (0, 0, 0)
    
    if key == "2": # Camera posistion two, side view of planets
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, 0, 70)
        camera.rotation = (0, -180, 0)

    if key == "3": # Camera posistion three, bird's eye view 
        for i in letters:
            held_keys[i] = 0
        camera.position = (0, defaultHeight, 0)
        camera.rotation_x = 90
        camera.rotation_z = 0
        camera.rotation_y = 0
    
    if key == "escape": # Pauses movement
        pause = not pause
    
    if key == "h": # Prints controls to the terminal 
        print(" ")
        for key in controls.keys():
            print(f"{Fore.GREEN + key}: {Fore.GREEN + controls[key]} {Fore.WHITE}")

    if key == "m": # Follows Mercury
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[0]] = 1

    if key == "v": # Follows Venus
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[1]] = 1

    if key == "e": # Follows Earth
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[2]] = 1

    if key == "r": # Follows Mars
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[3]] = 1

    if key == "j": # Follows Jupiter
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[4]] = 1

    if key == "s": # Follows Saturn
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[5]] = 1

    if key == "u": # Follows Uranus
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[6]] = 1

    if key == "n": # Follows Neptune
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[7]] = 1

    if key == "p": # Follows Pluto
        camera.y = trackingCameraHeight
        camera.rotation_x = 90
        for i in letters:
            held_keys[i] = 0
        held_keys[letters[8]] = 1

def update(): 
    # Global variables that are used, cannot be defined here because it would never increase
    global mercuryDeltaT, venusDeltaT, earthDeltaT, marsDeltaT, jupiterDeltaT, saturnDeltaT, uranusDeltaT, neptuneDeltaT, plutoDeltaT, cameraDeltaT
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

        if held_keys[letters[0]]:
            camera.x = math.cos(mercuryDeltaT) * mercury_radius
            camera.z = math.sin(mercuryDeltaT) * mercury_radius

        if held_keys[letters[1]]:
            camera.x = math.cos(venusDeltaT) * venus_radius
            camera.z = math.sin(venusDeltaT) * venus_radius

        if held_keys[letters[2]]:
            camera.x = math.cos(earthDeltaT) * earth_radius
            camera.z = math.sin(earthDeltaT) * earth_radius

        if held_keys[letters[3]]:
            camera.x = math.cos(marsDeltaT) * mars_radius
            camera.z = math.sin(marsDeltaT) * mars_radius

        if held_keys[letters[4]]:
            camera.x = math.cos(jupiterDeltaT) * jupiter_radius
            camera.z = math.sin(jupiterDeltaT) * jupiter_radius

        if held_keys[letters[5]]:
            camera.x = math.cos(saturnDeltaT) * saturn_radius
            camera.z = math.sin(saturnDeltaT) * saturn_radius

        if held_keys[letters[6]]:
            camera.x = math.cos(uranusDeltaT) * uranus_radius
            camera.z = math.sin(uranusDeltaT) * uranus_radius

        if held_keys[letters[7]]:
            camera.x = math.cos(neptuneDeltaT) * neptune_radius
            camera.z = math.sin(neptuneDeltaT) * neptune_radius

        if held_keys[letters[8]]:
            camera.x = math.cos(plutoDeltaT) * pluto_radius
            camera.z = math.sin(plutoDeltaT) * pluto_radius

    if held_keys["up arrow"] and not held_keys["shift"] and not held_keys["control"]:
        camera.y += .5

    if held_keys["down arrow"] and not held_keys["shift"] and not held_keys["control"]:
        camera.y -= .5
    
    if held_keys["left arrow"] and not held_keys["control"]:
        camera.x -= .5

    if held_keys["right arrow"] and not held_keys["control"]:
        camera.x += .5

    if held_keys["shift"]:
        if held_keys["up arrow"]:
            camera.z += .5

    if held_keys["shift"]:
        if held_keys["down arrow"]:
            camera.z -= .5

    if held_keys["control"]:
        if held_keys["up arrow"]:
            camera.rotation_x -= 1
    
    if held_keys["control"]:
        if held_keys["down arrow"]:
            camera.rotation_x += 1

    if held_keys["control"]:
        if held_keys["left arrow"]:
            camera.rotation_y -= 1
    
    if held_keys["control"]:
        if held_keys["right arrow"]:
            camera.rotation_y += 1

app = Ursina(position = (0, 0))

defaultHeight = 143
speedDiv = 5

global sunInfo, mercuryInfo, venusInfo, earthInfo, marsInfo, jupiterInfo, saturnInfo, neptuneInfo, uranusInfo, plutoInfo
with open(r'ursina-project\ursina-project\src\planets.json', "r") as current:
    file = json.load(current)
    uranusInfo = file["Sun"][0]
    mercuryInfo = file["Mercury"][0]
    venusInfo = file["Venus"][0]
    earthInfo = file["Earth"][0]
    marsInfo = file["Mars"][0]
    jupiterInfo = file["Jupiter"][0]
    saturnInfo = file["Saturn"][0]
    uranusInfo = file["Uranus"][0]
    neptuneInfo = file["Neptune"][0]
    plutoInfo = file["Pluto"][0]


# z = "mercury",x = "venus",c = "earth",b = "mars",l = "jupiter",k = "saturn",t = "uranus",y = "neptune",q = "pluto"]

letters = ["z","x","c","b","l","k","t","y","q"]

def sOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    print("".join([f"\n{key}, {uranusInfo[key]}" for key in uranusInfo.keys()]))

def mOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[0]] = 1
    print("".join([f"\n{key}, {mercuryInfo[key]}" for key in mercuryInfo.keys()]))

def vOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[1]] = 1
    print("".join([f"\n{key}, {venusInfo[key]}" for key in venusInfo.keys()]))

def eOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[2]] = 1
    print("".join([f"\n{key}, {earthInfo[key]}" for key in earthInfo.keys()]))

def rOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[3]] = 1
    print("".join([f"\n{key}, {marsInfo[key]}" for key in marsInfo.keys()]))

def jOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[4]] = 1
    print("".join([f"\n{key}, {jupiterInfo[key]}" for key in jupiterInfo.keys()]))


def stOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[5]] = 1
    print("".join([f"\n{key}, {saturnInfo[key]}" for key in saturnInfo.keys()]))

def uOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0  
    
    held_keys[letters[6]] = 1
    print("".join([f"\n{key}, {uranusInfo[key]}" for key in uranusInfo.keys()]))


def nOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[7]] = 1
    print("".join([f"\n{key}, {neptuneInfo[key]}" for key in neptuneInfo.keys()]))

def pOnClick():
    camera.position = (0, trackingCameraHeight, 0)
    camera.rotation_x = 90

    for i in letters:
        held_keys[i] = 0

    held_keys[letters[8]] = 1
    print("".join([f"\n{key}, {plutoInfo[key]}" for key in plutoInfo.keys()]))

sun = Entity(model = "sphere", scale = 2, texture = "sun.png", collider = 'box', on_click = sOnClick)
mercury = Entity(model = "sphere", scale = .8, texture = "mercury.jpg", collider = 'box', on_click = mOnClick)
venus = Entity(model = "sphere", scale = .9, texture = "venus.jpg", collider = 'box', on_click = vOnClick)
earth = Entity(model = "sphere", scale = 1, texture = "earth.jfif", collider = 'box', on_click = eOnClick)
moon = Entity(model = "sphere", scale = .3, texture = "moon.jpg")
mars = Entity(model = "sphere", scale = .7, texture = "mars.png", collider = 'box', on_click = rOnClick)
jupiter = Entity(model = "sphere", scale = 3, texture = "jupiter.jpg", collider = 'box', on_click = jOnClick)
saturn = Entity(model = "sphere", scale = 2.5, texture = "saturn.jpg", collider = 'box', on_click = stOnClick)
neptune = Entity(model = "sphere", scale = 1.2, texture = "neptune.jpg", collider = 'box', on_click = nOnClick)
uranus = Entity(model = "sphere", scale = 1.5, texture = "uranus.jfif", collider = 'box', on_click = uOnClick)
pluto = Entity(model = "sphere", scale = .5, texture = "pluto.jpg", collider = 'box', on_click = pOnClick)


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
    "1": "3D side view of Planets",
    "2": "Another 3D side view of Planets",
    "3": "Bird's Eye View of Solar System",
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