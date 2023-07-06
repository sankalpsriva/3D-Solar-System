import json
import numpy as np


class Constants:
    
    # Data
    with open(r'ursina-project\src\planets.json', "r") as current:
        file = json.load(current)
        sunInfo = file["Sun"][0]
        mercuryInfo = file["Mercury"][0]
        venusInfo = file["Venus"][0]
        earthInfo = file["Earth"][0]
        marsInfo = file["Mars"][0]
        jupiterInfo = file["Jupiter"][0]
        saturnInfo = file["Saturn"][0]
        uranusInfo = file["Uranus"][0]
        neptuneInfo = file["Neptune"][0]
        plutoInfo = file["Pluto"][0]
        controls = file["controls"]  
    letters = ["z","x","c","b","l","k","t","y","q"]


    # Orbit Constants
    mercuryDeltaT = np.pi
    venusDeltaT = np.pi
    earthDeltaT = np.pi
    moonDeltaT = np.pi
    marsDeltaT = np.pi
    jupiterDeltaT = np.pi
    saturnDeltaT = np.pi
    uranusDeltaT = np.pi
    neptuneDeltaT = np.pi
    plutoDeltaT = np.pi
    cameraDeltaT = np.pi
    speedDiv = 8
    
    rotationConstant = 50
    
    # Planet Radius and Star Radius
    spacing = 2
    mercuryRadius = 5
    venusRadius = 9
    earthRadius  = 13 
    marsRadius = 22
    jupiterRadius = 27 
    saturnRadius = 35
    uranusRadius = 45
    neptuneRadius = 55
    plutoRadius = 65
    starRadius = 500
    
    # Camera Constants
    trackingCameraHeight = 50
    defaultHeight = 300
    negate = 1
    
    
    # Booleans
    pause = False
    sideTrack = False

    
    
    