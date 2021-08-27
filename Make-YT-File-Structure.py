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

makeFolder(MAIN_FILE_PATH, nameOfVideo)

for folder in SUB_FOLDERS_TO_MAKE:
    makeFolder(os.path.join(MAIN_FILE_PATH, nameOfVideo), folder)

print("All your folders are made, enjoy making your YouTube Video :)")
