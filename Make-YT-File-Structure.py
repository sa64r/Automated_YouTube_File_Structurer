#!/usr/bin/python

import os

# CONSTANTS
MAIN_FILE_PATH = "E:\YouTube\Videos"
SUB_FOLDERS_TO_MAKE = ['Graphics', 'Raw', 'BRoll', 'Music', 'SFX', 'Thumbnail']

# User needs to enter these values
nameOfVideo = ""

# Makes a folder in a certain location


def makeFolder(path, folderName):
    fullPath = os.path.join(path, folderName)
    os.mkdir(fullPath)


# Prompts user to enter the name of the primary folder to make for a specific YT video.
while nameOfVideo == "":
    nameOfVideo = input("Enter the name of the video you're making: ")

print("Making file structure for %s..." % nameOfVideo)

# Creates main folder
makeFolder(MAIN_FILE_PATH, nameOfVideo)

# Creates all the sub folders
for folder in SUB_FOLDERS_TO_MAKE:
    makeFolder(os.path.join(MAIN_FILE_PATH, nameOfVideo), folder)

# Creates a Hitfilm project, where you can edit videos
hitfilmFile = nameOfVideo + ".hfp"
f = open(os.path.join(MAIN_FILE_PATH, nameOfVideo, hitfilmFile), "x")
f.close()

print("All your folders and files are made, enjoy making your YouTube Video :)")
print("Go to: " + os.path.join(MAIN_FILE_PATH, nameOfVideo))
os.system("pause")
