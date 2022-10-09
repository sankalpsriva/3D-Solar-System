from ursina import *
import json
import numpy as np
import math
from colorama import Fore
from constants import Constants 

def set():
    camera.y = Constants.trackingCameraHeight
    camera.rotation_x = 90
    for i in Constants.letters:
        held_keys[i] = 0
        
global root
def input(key):
    # Keyboard Presses
    if key == "1": # Camera posistion one, side view of planets
        set()
        camera.position = (0, 0, -70)
        camera.rotation = (0, 0, 0)
    
    if key == "2": # Camera posistion two, side view of planets
        set()
        camera.position = (0, 0, 70)
        camera.rotation = (0, -180, 0)

    if key == "3": # Camera posistion three, bird's eye view 
        set()
        camera.position = (0, Constants.defaultHeight, 0)
        camera.rotation_x = 90
        camera.rotation_z = 0
        camera.rotation_y = 0
    
    if key == "escape": # Pauses movement
        Constants.pause = not Constants.pause
    
    if key == "h": # Prints controls to the terminal 
        print(" ")
        for key in Constants.controls.keys():
            print(f"{Fore.GREEN + key}: {Fore.GREEN + Constants.controls[key]} {Fore.WHITE}")

    if key == "m": # Follows Mercury
        set()
        held_keys[Constants.letters[0]] = 1

    if key == "v": # Follows Venus
        set()
        held_keys[Constants.letters[1]] = 1

    if key == "e": # Follows Earth
        set()
        held_keys[Constants.letters[2]] = 1

    if key == "r": # Follows Mars
        set()
        held_keys[Constants.letters[3]] = 1

    if key == "j": # Follows Jupiter
        set()
        held_keys[Constants.letters[4]] = 1

    if key == "s": # Follows Saturn
        set()
        held_keys[Constants.letters[5]] = 1

    if key == "u": # Follows Uranus
        set()
        held_keys[Constants.letters[6]] = 1

    if key == "n": # Follows Neptune
        set()
        held_keys[Constants.letters[7]] = 1

    if key == "p": # Follows Pluto
        set()
        held_keys[Constants.letters[8]] = 1

def update(): 
    # Global variables that are used, cannot be defined here because it would never increase
    if not Constants.pause:
        Constants.mercuryDeltaT += 0.2012 / Constants.speedDiv # 0.02
        Constants.venusDeltaT += 0.1805 / Constants.speedDiv  # 0.03
        Constants.earthDeltaT += 0.15 / Constants.speedDiv  # 0.034
        Constants.marsDeltaT += 0.1 /  Constants.speedDiv  # 0.0415
        Constants.jupiterDeltaT += 0.07 / Constants.speedDiv
        Constants.saturnDeltaT += 0.0415 / Constants.speedDiv # 0.1
        Constants.uranusDeltaT += 0.034 / Constants.speedDiv # 0.15
        Constants.neptuneDeltaT += 0.03 / Constants.speedDiv # 0.185
        Constants.plutoDeltaT += 0.01 / Constants.speedDiv # 0.212
        Constants.cameraDeltaT += 0.015

        sun.rotation_y += time.dt * 20

        # Mercury orbit 
        mercury.x = math.cos(Constants.mercuryDeltaT) * Constants.mercuryRadius
        mercury.z = math.sin(Constants.mercuryDeltaT) * Constants.mercuryRadius
        mercury.rotation_y += time.dt * 50

        # Venus orbit 
        venus.x = math.cos(Constants.venusDeltaT) * Constants.venusRadius
        venus.z = math.sin(Constants.venusDeltaT) * Constants.venusRadius
        venus.rotation_y += time.dt * 50

        # Earth orbit    
        earth.x = math.cos(Constants.earthDeltaT) * Constants.earthRadius
        earth.z = math.sin(Constants.earthDeltaT) * Constants.earthRadius
        earth.rotation_y += time.dt * 50

        # Moon orbit, had to use earthDeltaT and added earth.x and earth.z to make it orbit around the earth
        moon.y = .5
        moon.x = math.cos(Constants.earthDeltaT) * (Constants.earthRadius - 4) + earth.x / 2.3
        moon.z = math.sin(Constants.earthDeltaT) * (Constants.earthRadius - 4) + earth.z / 2.3
        moon.rotation_y += time.dt * 50

        # Mars orbit
        mars.x = math.cos(Constants.marsDeltaT) * Constants.marsRadius
        mars.z = math.sin(Constants.marsDeltaT) * Constants.marsRadius
        mars.rotation_y += time.dt * 50

        # Jupiter orbit
        jupiter.x = math.cos(Constants.jupiterDeltaT) * Constants.jupiterRadius
        jupiter.z = math.sin(Constants.jupiterDeltaT) * Constants.jupiterRadius 
        jupiter.rotation_y += time.dt * 50

        # Saturn orbit
        saturn.x = math.cos(Constants.saturnDeltaT) * Constants.saturnRadius
        saturn.z = math.sin(Constants.saturnDeltaT) * Constants.saturnRadius
        saturn.rotation_y += time.dt * 50

        # Uranus orbit
        uranus.x = math.cos(Constants.uranusDeltaT) * Constants.uranusRadius
        uranus.z = math.sin(Constants.uranusDeltaT) * Constants.uranusRadius
        uranus.rotation_y += time.dt * 50

        # Neptune orbit
        neptune.x = math.cos(Constants.neptuneDeltaT) * Constants.neptuneRadius
        neptune.z = math.sin(Constants.neptuneDeltaT) * Constants.neptuneRadius
        neptune.rotation_y += time.dt * 50
        
        # Pluto orbit
        pluto.x = math.cos(Constants.plutoDeltaT) * Constants.plutoRadius
        pluto.z = math.sin(Constants.plutoDeltaT) * Constants.plutoRadius
        pluto.rotation_y += time.dt * 50

        # Camera tracking based on letter pressed
        if held_keys[Constants.letters[0]]:
            camera.x = math.cos(Constants.mercuryDeltaT) * Constants.mercuryRadius
            camera.z = math.sin(Constants.mercuryDeltaT) * Constants.mercuryRadius

        if held_keys[Constants.letters[1]]:
            camera.x = math.cos(Constants.venusDeltaT) * Constants.venusRadius
            camera.z = math.sin(Constants.venusDeltaT) * Constants.venusRadius

        if held_keys[Constants.letters[2]]:
            camera.x = math.cos(Constants.earthDeltaT) * Constants.earthRadius
            camera.z = math.sin(Constants.earthDeltaT) * Constants.earthRadius

        if held_keys[Constants.letters[3]]:
            camera.x = math.cos(Constants.marsDeltaT) * Constants.marsRadius
            camera.z = math.sin(Constants.marsDeltaT) * Constants.marsRadius

        if held_keys[Constants.letters[4]]:
            camera.x = math.cos(Constants.jupiterDeltaT) * Constants.jupiterRadius
            camera.z = math.sin(Constants.jupiterDeltaT) * Constants.jupiterRadius

        if held_keys[Constants.letters[5]]:
            camera.x = math.cos(Constants.saturnDeltaT) * Constants.saturnRadius
            camera.z = math.sin(Constants.saturnDeltaT) * Constants.saturnRadius

        if held_keys[Constants.letters[6]]:
            camera.x = math.cos(Constants.uranusDeltaT) * Constants.uranusRadius
            camera.z = math.sin(Constants.uranusDeltaT) * Constants.uranusRadius

        if held_keys[Constants.letters[7]]:
            camera.x = math.cos(Constants.neptuneDeltaT) * Constants.neptuneRadius
            camera.z = math.sin(Constants.neptuneDeltaT) * Constants.neptuneRadius

        if held_keys[Constants.letters[8]]:
            camera.x = math.cos(Constants.plutoDeltaT) * Constants.plutoRadius
            camera.z = math.sin(Constants.plutoDeltaT) * Constants.plutoRadius

    # Camera Controls 
    if held_keys["up arrow"] and not held_keys["shift"] and not held_keys["control"]:
        camera.y += .5

    if held_keys["down arrow"] and not held_keys["shift"] and not held_keys["control"]:
        camera.y -= .5
    
    if held_keys["left arrow"] and not held_keys["control"]:
        camera.x -= .5

    if held_keys["right arrow"] and not held_keys["control"]:
        camera.x += .5

    if held_keys["shift"] and held_keys["up arrow"]:
        camera.z += .5

    if held_keys["shift"] and held_keys["down arrow"]:
        camera.z -= .5

    if held_keys["control"] and held_keys["up arrow"]:
        camera.rotation_x -= 1
    
    if held_keys["control"] and held_keys["down arrow"]:
        camera.rotation_x += 1

    if held_keys["control"] and held_keys["left arrow"]:
        camera.rotation_y -= 1
    
    if held_keys["control"] and held_keys["right arrow"]:
        camera.rotation_y += 1

app = Ursina(position = (0, 0))

def sOnClick():
    set()
    print("".join([f"\n{key}, {Constants.sunInfo[key]}" for key in Constants.sunInfo.keys()]))

def mOnClick():
    set()
    
    held_keys[Constants.letters[0]] = 1
    print("".join([f"\n{key}, {Constants.mercuryInfo[key]}" for key in Constants.mercuryInfo.keys()]))

def vOnClick():
    set()
    
    held_keys[Constants.letters[1]] = 1
    print("".join([f"\n{key}, {Constants.venusInfo[key]}" for key in Constants.venusInfo.keys()]))

def eOnClick():
    set()
    
    held_keys[Constants.letters[2]] = 1
    print("".join([f"\n{key}, {Constants.earthInfo[key]}" for key in Constants.earthInfo.keys()]))

def rOnClick():
    set()
    
    held_keys[Constants.letters[3]] = 1
    print("".join([f"\n{key}, {Constants.marsInfo[key]}" for key in Constants.marsInfo.keys()]))

def jOnClick():
    set()

    held_keys[Constants.letters[4]] = 1
    print("".join([f"\n{key}, {Constants.jupiterInfo[key]}" for key in Constants.jupiterInfo.keys()]))


def stOnClick():
    set()
    
    held_keys[Constants.letters[5]] = 1
    print("".join([f"\n{key}, {Constants.saturnInfo[key]}" for key in Constants.saturnInfo.keys()]))

def uOnClick():
    set()
    
    held_keys[Constants.letters[6]] = 1
    print("".join([f"\n{key}, {Constants.uranusInfo[key]}" for key in Constants.uranusInfo.keys()]))


def nOnClick():
    set()
    
    held_keys[Constants.letters[7]] = 1
    print("".join([f"\n{key}, {Constants.neptuneInfo[key]}" for key in Constants.neptuneInfo.keys()]))

def pOnClick():
    set()
    
    held_keys[Constants.letters[8]] = 1
    print("".join([f"\n{key}, {Constants.plutoInfo[key]}" for key in Constants.plutoInfo.keys()]))

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
ring.color = color.rgb(186, 184, 110)

for i in range(1000):
    star = Entity(model = "sphere", scale = .8, color = color.white, texture = "sky_sunset")
    bStar = Entity(model = "sphere", scale = .4, color = color.white, texture = "sky_sunset")

    star.x = math.cos(i) * Constants.starRadius
    star.z = math.sin(i) * Constants.starRadius
    star.y = random.randint(-100, 100)

    bStar.x = random.randint(-100, 100)
    bStar.z = random.randint(-100, 100)
    bStar.y = -50

    bStar.color = color.rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    star.color = color.rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    

uRing = Entity(model=load_model('torus.obj'))
uRing.position = uranus.position
uRing.scale = uranus.scale - .1
uRing.scale_y = .3
uRing.rotation_x = 90
uRing.reparent_to(uranus)
uRing.color = color.rgb(28, 156, 195)


camera.position = (0, Constants.defaultHeight, 0)
camera.rotation_x = 90

Sky(texture = "download.jfif")

print(Fore.GREEN + "\nPress H For Controls\n" + Fore.WHITE)

window.size = (1920, 1080)
app.run()