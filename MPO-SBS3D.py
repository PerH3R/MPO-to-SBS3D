from PIL import Image
import os 
import sys
from pathlib import Path

# ARGS:
# Source directory '-s'; Default "./DCIM" 
# Destination directory '-d'; Default "./DCIM-SBS" 

MPOfolder = os.sep.join([".", "DCIM"])
SBSfolder = os.sep.join([".", "DCIM-SBS"])
argList = [MPOfolder, SBSfolder]


def is_path_valid(path: str) -> bool:
    # Check if a path is syntactically valid (OS-agnostic).
    try:
        # Attempt to resolve the path (doesn't require existence)
        Path(path).resolve(strict=False)
        return True
    except (OSError, ValueError):
        return False


lastArg = ""
for arg in sys.argv:
    if lastArg == "-s" and is_path_valid(str(arg)):
        argList[0] = str(arg)
    if lastArg == "-d" and is_path_valid(str(arg)):
        argList[1] = str(arg)
    lastArg = arg
    

def list_files_recursive(path, MPOfiles) -> list:
    for entry in os.listdir(path):
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            list_files_recursive(fullPath, MPOfiles)
        else:
            # add all found .MPO files to a list
            if entry.endswith(".MPO"):
                MPOfiles.append(os.path.normpath(fullPath))
    return MPOfiles

def save_image(ogFilepath, imageData, exifData):
    # construct filepath for converted image
    newFilepath = ogFilepath.split(os.sep)#[-1][5:8]
    newFilepath[0] = argList[1]
    newFilepath[-1] = newFilepath[-1][:-4] + ".JPG"
    newFilepath = os.path.join(*newFilepath)

    # save the SBS image to the new location with exifdata intact
    fileDir = os.path.dirname(newFilepath)
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    imageData.save(newFilepath, quality=100, optimize=True, exif=exifData)

def convert_image(ogFilepath):
    # load images
    imRight = Image.open(ogFilepath)
    imLeft = Image.open(ogFilepath)
    imRight.size
    imLeft.seek(1)
    imSBS = imRight.copy()

    # save exifdata to copy into SBS image after conversion
    exifData = imLeft.getexif()
    
    # make room for second image and paste the image for the other eye
    imSBS = imSBS.resize(((imRight.width*2), imRight.height))
    imSBS.paste(imLeft,(0,0))
    imSBS.paste(imRight, (imRight.width, 0))

    save_image(ogFilepath, imSBS, exifData)

def main():
    MPOfiles = list_files_recursive(argList[0], [])
    for path in MPOfiles:
        convert_image(path)
        pass




main()

print("done")
