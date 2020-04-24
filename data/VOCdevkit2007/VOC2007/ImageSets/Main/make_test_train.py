import sys
import numpy as np

image_names_file = sys.argv[1]
train_val_file = sys.argv[2]
test_file = sys.argv[3]

image_file = open(image_names_file, "r")
image_names = image_file.readlines()

train_val_imgs = []
test_imgs = []

for image_name in image_names:
    image_name_arr = image_name.split("_")
    image_num = int(image_name_arr[-1])
    if str(image_name_arr[1]) == "video":
        if image_num > 3000:
            test_imgs.append(image_name)
        else:
            train_val_imgs.append(image_name)
    else:
        train_val_imgs.append(image_name)

image_file.close()

trainvalFile = open(train_val_file, "w")
for imgs in train_val_imgs:
    trainvalFile.write(str(imgs))

trainvalFile.close()

testFile = open(test_file, "w")
for imgs in test_imgs:
    testFile.write(str(imgs))

testFile.close()
