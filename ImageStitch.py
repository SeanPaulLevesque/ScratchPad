import urllib.request

from os import path
from PIL import Image

# scrape images from the website
# file names are formatted "Zoom-Xcoord-Ycoord"
# images are stored in seemingly random folders, can't figure it out, just check them all for every file

# generate images list
images = []
for g in range(1,11):
    for x in range(1,54):
        for y in range(1,73):
            images.append("https://s3.eu-west-2.amazonaws.com/mapshow/Boston1/TileGroup" + str(g) + "/7-" + str(x) + "-" + str(y) + ".jpg")



for url in images:
    try:
        result = urllib.request.urlretrieve(url, "images/7-"+ str(x) + "-" + str(y) + ".jpg")
    except IOError as e:
        print('??????', e)


# set the size of the stitched together image
for x in range(100,1,-1):
    if path.exists("images/7-" + str(x) + "-1.jpg"):
        maxX = x - 1
        break

for y in range(100,1,-1):
    if path.exists("images/7-1-" + str(y) + ".jpg"):
        maxY = y - 1
        break

im = Image.open("images/7-2-2.jpg")
(width, height) = im.size
result_width = width * maxX
result_height = height * maxY

result = Image.new('RGB', (result_width, result_height))

# open each image and paste it into the final image in the correct position
for y in range(1,maxY):
    for x in range(1,maxX):
        try:
            im = Image.open("images/7-" + str(x+1) + "-" + str(y+1) + ".jpg")
        except IOError as e:
            continue
        result.paste(im=im, box=((x-1) * width, (y-1) * height))

result.save("stitched/all.jpg", "JPEG")

program = "done"


# while x < 53:
#
#     im1 = Image.open("images/7-" + str(x) + "-2.jpg")
#     im2 = Image.open("images/7-" + str(x) + "-3.jpg")
#     im3 = Image.open("images/7-" + str(x) + "-4.jpg")
#     im4 = Image.open("images/7-" + str(x) + "-5.jpg")
#     #im5 = Image.open("images/7-" + str(x) + "-6.jpg")
#
#     (width1, height1) = im1.size
#     (width2, height2) = im2.size
#     (width3, height3) = im3.size
#     (width4, height4) = im4.size
#     #(width5, height5) = im5.size
#
#     result_width = max(width2, width3, width4)
#     result_height = height1 + height2 + height3 + height4 + height5
#
#     result = Image.new('RGB', (result_width, result_height))
#     result.paste(im=im1, box=(0, 0))
#     result.paste(im=im2, box=(0, height1))
#     result.paste(im=im3, box=(0, height1 + height2))
#     result.paste(im=im4, box=(0, height1 + height2 + height3))
#     result.paste(im=im5, box=(0, height1 + height2 + height3 + height4))
#
#     result.save("stitched/" + str(x) + ".jpg", "JPEG")
#     x = x + 1

