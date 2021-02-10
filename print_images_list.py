import os
import re
import glob
images_list = glob.glob("/home/rinzler/darknet/data/obj/images/*.png")
print(images_list)

file = open("/home/rinzler/darknet/data/train.txt", "w")
file.write("\n".join(images_list))
file.close()


