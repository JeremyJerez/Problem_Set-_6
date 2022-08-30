# Python_Intro
# Problem Set 6
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "CS50 P-Shirt" problem
"""
import sys
from os.path import splitext

from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exists")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(imagefile, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False or check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extension(file):
    if file in [".jpg", ".jepg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()
