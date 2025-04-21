import cv2
import json

file_name = "mihoyo_logo.png"
img = cv2.imread(file_name)
print(img.shape)
img_y = img.shape[0]
img_x = img.shape[1]

data_dict = []

for y in range(img_y):
    this_y = []
    for x in range(img_x):
        print(f"{x},{y}", img[y, x])
        b, g, r = img[y, x]
        this = int(r), int(g), int(b)
        this_y.append(this)
    data_dict.append(this_y)
# print(len(data_dict))

with open(file_name.split(".")[0]+".json", "w") as f:
    f.write(json.dumps(data_dict))
