import urllib.request
import os
import threading

from os import path
from PIL import Image

results = []
def getter(url, dest):
    try:
        results.append(urllib.request.urlretrieve(url, dest))
    except IOError as e:
        print('??????', e)
    except Exception as e:
        print('?? ?', e)


def findmaxY():
    for y in range(100,1,-1):
        for x in range(100,1,-1):
            if path.exists("images/7-" + str(x) + "-" + str(y) + ".jpg"):
                maxX = x
                return maxX


def findmaxX():
    for x in range(100, 1, -1):
        for y in range(100, 1, -1):
            if path.exists("images/7-" + str(x) + "-" + str(y) + ".jpg"):
                maxY = y
                return maxY

# scrape images from the website
# file names are formatted "Zoom-Xcoord-Ycoord"
# images are stored in seemingly random folders, can't figure it out, just check them all for every file

# generate images list
images = []
for g in range(6, 21):
    for x in range(1, 55):
        for y in range(1, 75):
            images.append("https://s3.eu-west-2.amazonaws.com/mapshow/Boston2/TileGroup" + str(g) + "/7-" + str(x) + "-" + str(y) + ".jpg")

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
        maxX = x - 1
        break

for y in range(100,1,-1):
    if path.exists("images/7-1-" + str(y) + ".jpg"):
        maxY = y - 1
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

result.save("stitched/all2.jpg", "JPEG")

program = "done"
