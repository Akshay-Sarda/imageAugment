import cv2
import matplotlib.pyplot as plt
import re
import os
from utils import *
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# test = "./10000718_1_on_RelineCore1LevelB"
test = filedialog.askopenfilenames()[0]
testName = re.search(r"\/(\w+)(?!.*\/)", test)[1]

img = cv2.imread(test)
print(testName)

toolBoundingBoxData = f"{testName}.txt"

with open(toolBoundingBoxData) as f:
    lines = f.readlines()

toolLabel, *dimensions = lines[0].split()

width, height, x, y = [int(dimension) for dimension in dimensions]
print(toolLabel, width, height, x, y)

cv2.rectangle(
    img,
    (x, y),
    (x + width, y + height),
    color=(0, 100, 200),
    thickness=2,
)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey()
