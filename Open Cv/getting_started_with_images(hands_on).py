# -*- coding: utf-8 -*-
"""Getting_Started_With_Images(Hands On).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e3tj59OfYlR9O3BYnRcXeu4NGX7VIYSx

Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve
from IPython.display import Image
# %matplotlib inline

"""Download Assets"""

def download_and_unzip(url, save_path):
  print(f"Downloading and extracting assets....", end="")

  #Downloading zipfile using urllib package.
  urlretrieve(url, save_path)

  try:
    #Extracting zipfile using the zipfile package.
    with ZipFile(save_path) as z:
      #Extract ZIP file contents in the same directory.
      z.extractall(os.path.spilt(save_path)[0])

      print("Done")

  except Exception as e:
    print("\nInvalid file.", e)

URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

# Download if assest ZIP does not exists.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

"""The opencv_bootcamp_assets_NB1.zip file includes also contains the additional display_image.py python script.

Display Image Directly

we will the following as our sample images.We will use the ipython image function to load and display the image.
"""

#Display 18x18 pixel image
Image(filename="checkerboard_18x18.png")

#Display 84x84 pixel image
Image(filename="checkerboard_84x84.jpg")

"""Reading Images Using Opencv"""

#Reading the image as grayscale
cb_img = cv2.imread("checkerboard_18x18.png", 0)

#print the image data(pixel values), element of a 2D numpy array.
#Each pixel value is 8-bits[0-255]
print(cb_img)

"""Display Image Attributes"""

#print the size of image
print("Image size (H,W) is:", cb_img.shape)

#print data-type of image
print("Data type of image is:", cb_img.dtype)

"""Display Images Using Matplotlib"""

#display image
plt.imshow(cb_img)

"""What Happened?

Even though the image was read in as a grayscale image, it won't necessarily display in grayscale when using imshow(). matplotlib using defferent color maps and it's pissible that the gray scale color map is not set.
"""

#set color to gray scale for proper rendering
plt.imshow(cb_img, cmap="gray")

"""Another Example"""

#Read image as grayscale
cb_img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)

#print the image
print(cb_img_fuzzy)

#display the image as grayscale
plt.imshow(cb_img_fuzzy, cmap="gray")

"""Working with Color Images"""

#Read and display coca-cola logo.
Image("coca-cola-logo.png")

"""Read and display color image."""

#Read Image
coke_img = cv2.imread("coca-cola-logo.png")

#print the size of an image
print("Image size (H,W,C) is:", coke_img.shape)

#print data-type of image
print("The data-type of image is:", coke_img.dtype)

"""Display the image"""

plt.imshow(coke_img)

"""What Happened?
The color displayed above is different from the actual image.This is beacause matplotlib expects the image in RGB format whereas opencv stores the image in BGR format.Thus, for correct display we need to reverse the channels of the image.
"""

coke_img_channels_reversed = coke_img[:, :, ::-1]
plt.imshow(coke_img_channels_reversed)

#split the image into the B-G-R components
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)

#show the channels
plt.figure(figsize=(20,5))

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

#merge the individual channels into the bgr image
imgMerged = cv2.merge((b, g, r))

#show the merged output
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")

"""Converting to different color spaces

Changing from BGR to RGB
"""

#opencv stores color channels in a different order than most other applications(BGR Vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)

"""Changing to HSV color space"""

img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

#split the image into the b, g, r components
h,s,v = cv2.split(img_hsv)

#show the channels
plt.figure(figsize = [20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original")

"""Modifying individual channel"""

h_new = h + 10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

#show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V channel")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original")

"""Saving Images"""

#save the image
cv2.imwrite("New_Zealand_Lake_Saved.png", img_NZ_bgr)

Image(filename='New_Zealand_Lake_Saved.png')

#read the image as color
img_NZ_bgr = cv2.imread("New_Zealand_Lake_Saved.png", cv2.IMREAD_COLOR)
print("img_NZ_bgr shape (H,W,C) is:", img_NZ_bgr.shape)

#read the image as grayscaled
img_NZ_gry = cv2.imread("New_Zealand_Lake_Saved.png", cv2.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H,w) is:", img_NZ_gry.shape)