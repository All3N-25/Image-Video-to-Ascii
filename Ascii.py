import cv2
import os
import numpy as np
import time

SYMBOLS = [" ", ".", "i", "c", "o", "P", "O", "?", "&", "■"]
THRESHOLDS = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225]

def generate_ascii(img):
    """
    Returns the numeric coded image.
    Basically the 2D Array of the image.
    """

    height, width = img.shape
    #DOWNSCALLING | TO FIT INTO THE CONSOLE | Adjust If Necessary
    new_height = height // 8
    new_width = width // 4
    resize_img = cv2.resize(img, (new_width,new_height))

    """
    [
        [170, 123, 10],
        [21, 0, 105],
        [255,255,255]
    ]
    """

    thresh_img = np.zeros(resize_img.shape, dtype=np.uint8)

    """
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    """

    for i, threshold in enumerate(THRESHOLDS):

        thresh_img[resize_img > threshold] = i

    return thresh_img

def print_Symbols(array):
    """
    Filling the symbols in-place of the numbers
    """

    for row in array:
        for i in row:
            print(SYMBOLS[i], end ="")
        print("")

if __name__ == "__main__":

    #Getting the image data
    path = './Pictures/NahIdWin.jpg'
    img = cv2.imread(path, 0)

    height, width = img.shape

    #print(height , width)

    #Convert to ASCII
    ascii_art = generate_ascii(img)

    print_Symbols(ascii_art)

    #Using Video
    #vid = cv2.VideoCapture('./Video/.mp4')

    #while True:

        #ret, frame = vid.read()

        #if not ret:
            #break

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #ascii_art = generate_ascii(gray)
        #print_Symbols(ascii_art)

        #time.sleep(0.06)

    #USING Camera
    #cam = cv2.VideoCapture(0)
    

    #while True:
    #    ret, frame = cam.read()
    #    if not ret:
    #        continue

    #    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #    ascii_art = generate_ascii(gray)
    #    flipped = cv2.flip(ascii_art, 1)
    #    print_Symbols(flipped)
    


