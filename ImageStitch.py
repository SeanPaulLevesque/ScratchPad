import urllib.request
import os
import threading

from os import path
from PIL import Image


Image.MAX_IMAGE_PIXELS = None

im1 = Image.open("stitched/all.jpg")
im2 = Image.open("stitched/all2.jpg")

(width1, height1) = im1.size
(width2, height2) = im2.size
box1 = (0,0,width1-250,height1-250)
im1 = im1.crop(box1)
box2 = (281,281,width2,height2)
im2 = im2.crop(box2)
result_width = width1 + width2
result_height = max(height1,height2)

result = Image.new('RGB', (result_width, result_height))

result.paste(im=im1, box=(0, 0))
result.paste(im=im2, box=(width1-400, 178))

result.save("stitched/all_new.jpg", "JPEG")

program = "done"















results = []
def getter(url, dest):
    try:
        results.append(urllib.request.urlretrieve(url, dest))
    except IOError as e:
        print('??????', e)
    except Exception as e:
        print('?? ?', e)

# scrape images from the website
# file names are formatted "Zoom-Xcoord-Ycoord"
# images are stored in seemingly random folders, can't figure it out, just check them all for every file

# generate images list
images = []
for g in range(5, 21):
    for x in range(1, 53):
        for y in range(1, 46):
            images.append("https://s3.eu-west-2.amazonaws.com/mapshow/Boston3/TileGroup" + str(g) + "/7-" + str(x) + "-" + str(y) + ".jpg")

# request url from the list
# only run 100 threads at a time because threads do not like url.split
threads = []
thread_count = 0
for url in images:
    dest = "images/" + url.split("/")[6]
    t = threading.Thread(target=getter, args=(url, dest))
    t.start()
    threads.append(t)
    thread_count = thread_count + 1
    if thread_count == 100:
        [x.join() for x in threads]
        thread_count = 0

[x.join() for x in threads]


# set the size of the stitched together image
for x in range(100,1,-1):
    if path.exists("images/7-" + str(x) + "-1.jpg"):
        maxX = x
        break

for y in range(100,1,-1):
    if path.exists("images/7-1-" + str(y) + ".jpg"):
        maxY = y
        break

im = Image.open("images/7-2-2.jpg")
(width, height) = im.size
result_width = width * (maxX)
result_height = height * (maxY)

result = Image.new('RGB', (result_width, result_height))

# open each image and paste it into the final image in the correct position
for y in range(0,maxY+1):
    for x in range(0,maxX+1):
        try:
            im = Image.open("images/7-" + str(x) + "-" + str(y) + ".jpg")
        except IOError as e:
            continue
        result.paste(im=im, box=((x-1) * width, (y-1) * height))

result.save("stitched/all3.jpg", "JPEG")

program = "done"
