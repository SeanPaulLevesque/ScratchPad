import urllib.request

# x=15
# y=2
# g=10
# while g <11:
#     x = 1
#     while x < 54:
#         y=1
#         while y <73:
#             filestring = "https://s3.eu-west-2.amazonaws.com/mapshow/Boston1/TileGroup" + str(g) + "/7-" + str(x) + "-" + str(y) + ".jpg"
#             #filestring = "https://s3.eu-west-2.amazonaws.com/mapshow/Boston1/TileGroup20/7-0-71.jpg"
#             try:
#                 result = urllib.request.urlretrieve(filestring, "images/7-"+ str(x) + "-" + str(y) + ".jpg")
#             except IOError as e:
#                 print('??????', e)
#             except Exception as e:
#                 print('?? ?', e)
#             y=y+1
#         x = x + 1
#     g = g + 1


# from PIL import Image
#
# im1 = Image.open("stitched/1.jpg")
# (width1, height1) = im1.size
#
# result_width = width1 * 53
# result_height = height1
# result = Image.new('RGB', (result_width, result_height))
# result.paste(im=im1, box=(0, 0))
#
# for x in range(1,53):
#     im = Image.open("stitched/backup/" + str(x) + ".jpg")
#     result.paste(im=im, box=(x * width1, 0))
#
# result.save("stitched/backup/all.jpg", "JPEG")
#
# program = "done"
#

x = 33
from PIL import Image

while x < 53:

    im1 = Image.open("images/7-" + str(x) + "-20.jpg")
    im2 = Image.open("images/7-" + str(x) + "-21.jpg")
    im3 = Image.open("images/7-" + str(x) + "-22.jpg")
    im4 = Image.open("images/7-" + str(x) + "-23.jpg")
    im5 = Image.open("images/7-" + str(x) + "-24.jpg")

    (width1, height1) = im1.size
    (width2, height2) = im2.size
    (width3, height3) = im3.size
    (width4, height4) = im4.size
    (width5, height5) = im5.size

    result_width = max(width1, width2, width3, width4, width5)
    result_height = + height2 + height3 + height4 + height5

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=im1, box=(0, 0))
    result.paste(im=im2, box=(0, height1))
    result.paste(im=im3, box=(0, height1 + height2))
    result.paste(im=im4, box=(0, height1 + height2 + height3))
    result.paste(im=im5, box=(0, height1 + height2 + height3 + height4))

    result.save("stitched/" + str(x) + ".jpg", "JPEG")
    x = x + 1


program = "done"

while x < 33:

    im1 = Image.open("images/7-" + str(x) + "-2.jpg")
    im2 = Image.open("images/7-" + str(x) + "-3.jpg")
    im3 = Image.open("images/7-" + str(x) + "-4.jpg")
    im4 = Image.open("images/7-" + str(x) + "-5.jpg")
    #im5 = Image.open("images/7-" + str(x) + "-6.jpg")

    (width1, height1) = im1.size
    (width2, height2) = im2.size
    (width3, height3) = im3.size
    (width4, height4) = im4.size
    #(width5, height5) = im5.size

    result_width = max(width2, width3, width4)
    result_height = height1 + height2 + height3 + height4 + height5

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=im1, box=(0, 0))
    result.paste(im=im2, box=(0, height1))
    result.paste(im=im3, box=(0, height1 + height2))
    result.paste(im=im4, box=(0, height1 + height2 + height3))
    result.paste(im=im5, box=(0, height1 + height2 + height3 + height4))

    result.save("stitched/" + str(x) + ".jpg", "JPEG")
    x = x + 1


program = "done"

#
# x = 1
# y = 2
# g = 6
# while g < 7:
#     x = 1
#     while x < 54:
#         y = 1
#         while y < 73:
#             filestring = "https://s3.eu-west-2.amazonaws.com/mapshow/Boston1/TileGroup" + str(g) + "/7-" + str(
#                 x) + "-" + str(y) + ".jpg"
#             # filestring = "https://s3.eu-west-2.amazonaws.com/mapshow/Boston1/TileGroup20/7-0-71.jpg"
#             try:
#                 result = urllib.request.urlretrieve(filestring, "images/7-" + str(x) + "-" + str(y) + ".jpg")
#             except IOError as e:
#                 print('??????', e)
#             except Exception as e:
#                 print('?? ?', e)
#             y = y + 1
#         x = x + 1
#     g = g + 1